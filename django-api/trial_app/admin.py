from django.contrib import admin

# Register your models here.
from .models import UserInfo, Task
admin.site.register(UserInfo)
admin.site.register(Task)
