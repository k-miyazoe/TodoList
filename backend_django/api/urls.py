from django.urls import path
from . import views
from .views import *

app_name = "api"

urlpatterns = [
    #sample
    path('get/', views.get_todo, name='get_todo'),
    path('post/', views.post_todo, name='post_todo'),
    path('delete/',views.delete_todo, name='delete_todo'),
    #userinfo
    path('get_my_user/', views.get_my_user, name='get_my_user'),
    path('post_my_user/', views.post_my_user, name='post_my_user'),

    #selialize
    path('users/', UserList.as_view()),
    path('create-users/', UserCreate.as_view()),
    path('users/<pk>/', UserRetrieveUpdate.as_view()),

    path('profile/', UserProfileCreate.as_view()),
    path('profile/<pk>', UserProfileRetrieveUpdate.as_view()),

    path('todo/', TodoListCreate.as_view()),
    path('todo/<pk>', TodoListRetrieveUpdateDestroy.as_view()),
]