from django.conf.urls import url
from django.urls import path
from .views import index,todolist,add_todolist,new_todolist,add_todo,overview,login_view, logout_view,register
app_name = 'To_Do_App'
urlpatterns = [
    path('login/', login_view.as_view(), name='login'),
    path('logout/', logout_view.as_view(), name='logout'),
    path('register/', register.as_view(), name='register'),
    path('index', index.as_view(), name='index'),
    path('todolist/<int:todolist_id>/', todolist.as_view(), name='todolist'),
    path('todolist/new/', new_todolist.as_view(), name='new_todolist'),
    path('todolist/add/', add_todolist.as_view(), name='add_todolist'),
    path('todo/add/<int:todolist_id>/', add_todo.as_view(), name='add_todo'),
    path('todolists/', overview.as_view(), name='overview'),
]