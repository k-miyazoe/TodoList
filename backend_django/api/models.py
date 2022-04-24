from django.db import models

#userからUserProfileに変更
class UserProfile(models.Model):
    name          = models.CharField(max_length=30)
    email_address = models.EmailField()
    icon          = models.TextField(null=True)
    best_contact  = models.CharField(max_length=50,null=True)
    now_state     = models.CharField(max_length=40,null=True)
    dev_experiece = models.TextField(null=True)
    active_type   = models.BooleanField(null=True)
    created       = models.DateTimeField(auto_now_add=True) #追加

class Level_Of_Skill(models.Model):
    level_of_skill = models.CharField(max_length=50)

class Language(models.Model):
    language = models.CharField(max_length=30)
    skill_id = models.ForeignKey(Level_Of_Skill, on_delete=models.CASCADE)
    uid      = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

class Field(models.Model):
    field    = models.CharField(max_length=30)
    skill_id = models.ForeignKey(Level_Of_Skill, on_delete=models.CASCADE)
    uid      = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
   
class Question(models.Model):
    time        = models.DateTimeField(verbose_name='作成日時', auto_now_add=True)
    tag         = models.CharField(max_length=20)
    title       = models.CharField(max_length=30)
    error       = models.TextField()
    image       = models.TextField()
    source_code = models.TextField()
    challenge   = models.TextField(null=True)
    fictional   = models.TextField(null=True)
    no_idea     = models.TextField(null=True)
    uid         = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

class Answer(models.Model):
    time        = models.DateTimeField(verbose_name='作成日時', auto_now_add=True)
    title       = models.CharField(max_length=30)
    content     = models.TextField()
    uid         = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    stamp       = models.CharField(max_length=30)
    question_id = models.ForeignKey(Question, on_delete=models.CASCADE)
    test        = models.CharField(max_length=200)

class Todo(models.Model):
    task = models.CharField(max_length=255, unique=True)
    due = models.DateTimeField()
    done = models.BooleanField()
    #uid,id

    def __str__(self):
        return self.task

    