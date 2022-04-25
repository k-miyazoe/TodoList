#用意されてるUserモデル
from django.contrib.auth.models import User
#自分で作ったUserProfileモデル
from .models import UserProfile,Todo

from rest_framework import serializers

#用意されているUserモデルを利用
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'username',
                  'password', 'is_active', 'is_superuser')
        #idを更新不可にできる
        read_only_fields = ('id',)


#USERプロフィールモデルとして扱う
class UserProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['name','email_address','best_contact','now_state','dev_experiece','active_type','created']

class TodoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Todo
        fields = ['task','due','done']
