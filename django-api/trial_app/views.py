from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets
from .models import UserInfo, Task
from .serializer import UserInfoSerializer, TaskSerializer
class UserInfoViewSet(viewsets.ModelViewSet):
    # モデルのオブジェクトを取得
    queryset = UserInfo.objects.all()
    # シリアライザーを取得
    serializer_class = UserInfoSerializer

class TaskViewSet(viewsets.ModelViewSet):
    # モデルのオブジェクトを取得
    queryset = Task.objects.all()
    # シリアライザーを取得
    serializer_class = TaskSerializer
