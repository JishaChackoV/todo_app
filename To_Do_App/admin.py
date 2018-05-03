# Register your models here.
from django.contrib import admin
from.models import Profile
from.models import TodoList
from.models import Todo
admin.site.register(Profile)
admin.site.register(TodoList)
admin.site.register(Todo)
