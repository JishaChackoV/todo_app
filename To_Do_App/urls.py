from django.urls import path
from django.conf.urls import url
import To_Do_App
from To_Do_App import views

app_name = 'To_Do_App'
urlpatterns = [
    path('todo', views.Todo, name="index"),
    path('todolist', views.TodoList, name="todolist"),
    path('registration', views.RegisterUserView.as_view(), name="reg"),
    path('login', views.LoginUserView.as_view(), name="login"),
]