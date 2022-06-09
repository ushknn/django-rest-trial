from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from .models import UserInfo, Task
class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInfo
        # json で出力するフィールド
        fields = ('id','user_name', 'birth_day','age','created_at')

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        # json で出力するフィールド
        fields = ('id','task_detail')
