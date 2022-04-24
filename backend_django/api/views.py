import json
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render,redirect
from django.http import JsonResponse, HttpResponseServerError

from rest_framework import generics, permissions
from django.contrib.auth.models import User
from .models import Todo,UserProfile
from .serializers import UserSerializer,UserProfileSerializer
from rest_framework import viewsets
from django.utils.decorators import method_decorator

#User
class UserList(generics.ListAPIView):
    queryset = User.objects.all().order_by('first_name')
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticated,)


class UserCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticated,)
    #permission_classes = (permissions.IsAdminUser, )

#getなら特定のレコード取得,putなら特定のレコード更新

class UserRetrieveUpdate(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticated, )



#UserProfile
class UserProfileCreate(generics.ListCreateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = (permissions.IsAuthenticated, )

class UserProfileRetrieveUpdate(generics.RetrieveUpdateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = (permissions.IsAuthenticated, )




def get_todo(request):
    todos = Todo.objects.all().order_by("due").values()
    todolist = list(todos)
    return JsonResponse(todolist, safe=False)

@csrf_exempt
def post_todo(request):
    if request.method == 'POST' and request.body:
        json_dict = json.loads(request.body)
        task = json_dict['task']
        due = json_dict['due']
        done = json_dict['done']
        todos = Todo.objects.filter(task=task)
        #taskがdbに存在しない場合
        if not todos:
            Todo.objects.create(task=task, due=due, done=done)
        #taskがdbに存在する場合
        else:
            todos[0].due=due
            todos[0].done=done
            todos[0].save()
        return JsonResponse(json_dict)
    else:
        return HttpResponseServerError()

@csrf_exempt
def delete_todo(request):
    response = json.loads(request.body)
    task = Todo.objects.get(id=response.get('id'))
    task.delete()
    return JsonResponse({"result": "ok"})

#userの固有パラメーターを取得したい
def get_my_user(request):
    user = User.objects.all().order_by("id").values()
    user1 = list(user)
    # user = User.objects.all()
    # user = User.objects.all().values()
    return JsonResponse(user1, safe=False)

@csrf_exempt
def post_my_user(request):
    if request.method == 'POST' and request.body:
        json_dict = json.loads(request.body)
        name = json_dict['name']
        email_address = json_dict['email_address']
        # icon = json_dict['icon']
        best_contact = json_dict['best_contact']
        now_state = json_dict['now_state']
        dev_experiece = json_dict['dev_experiece']
        # active_type = json_dict['active_type']
        active_type = True
        user = User.objects.filter(name=name)
        #ユーザー情報がdbに存在しない場合
        if not user:
            User.objects.create(name=name, email_address=email_address, best_contact=best_contact, now_state=now_state, dev_experiece=dev_experiece, active_type=active_type)
        #ユーザー情報がdbに存在する場合->更新作業
        else:
            user[0].email_address=email_address
            # user[0].icon=icon
            user[0].best_contact=best_contact
            user[0].now_state=now_state
            user[0].dev_experiece=dev_experiece
            user[0].active_type=active_type
            user[0].save()
        return JsonResponse(json_dict)
    else:
        return HttpResponseServerError()
