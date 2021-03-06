# Generated by Django 3.1 on 2022-04-24 23:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Level_Of_Skill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level_of_skill', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task', models.CharField(max_length=255, unique=True)),
                ('due', models.DateTimeField()),
                ('done', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email_address', models.EmailField(max_length=254)),
                ('icon', models.TextField(null=True)),
                ('best_contact', models.CharField(max_length=50, null=True)),
                ('now_state', models.CharField(max_length=40, null=True)),
                ('dev_experiece', models.TextField(null=True)),
                ('active_type', models.BooleanField(null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(auto_now_add=True, verbose_name='作成日時')),
                ('tag', models.CharField(max_length=20)),
                ('title', models.CharField(max_length=30)),
                ('error', models.TextField()),
                ('image', models.TextField()),
                ('source_code', models.TextField()),
                ('challenge', models.TextField(null=True)),
                ('fictional', models.TextField(null=True)),
                ('no_idea', models.TextField(null=True)),
                ('uid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.userprofile')),
            ],
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language', models.CharField(max_length=30)),
                ('skill_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.level_of_skill')),
                ('uid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.userprofile')),
            ],
        ),
        migrations.CreateModel(
            name='Field',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('field', models.CharField(max_length=30)),
                ('skill_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.level_of_skill')),
                ('uid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.userprofile')),
            ],
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(auto_now_add=True, verbose_name='作成日時')),
                ('title', models.CharField(max_length=30)),
                ('content', models.TextField()),
                ('stamp', models.CharField(max_length=30)),
                ('test', models.CharField(max_length=200)),
                ('question_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.question')),
                ('uid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.userprofile')),
            ],
        ),
    ]
