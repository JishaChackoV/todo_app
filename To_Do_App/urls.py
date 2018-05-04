from django.conf.urls import url
from django.urls import path
from .views import ToDoCreateView, List_todo

app_name = 'To_Do_App'
urlpatterns = [
    path('index', ToDoCreateView.as_view(), name='index'),
   # url(r'^$,todo/delete/(?P<id>\d+)/$',todo_delete.as_view(),name='todo_delete'),
    path('todo/add/<int:todolist_id>/',List_todo.as_view(), name='add_todo'),
]