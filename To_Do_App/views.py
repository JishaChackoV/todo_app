from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponseRedirect
from django.views.generic import CreateView

from .models import Todo, TodoList
from .forms import TodoForm


# def login_view(request):
#     if request.method == 'POST':
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             user = authenticate(
#                 username=request.POST['username'],
#                 password=request.POST['password']
#             )
#             if user is not None:
#                 if user.is_active:
#                     login(request, user)
#                     return redirect('index')
#         else:
#             return render(request, 'login.html', {'form': form})
#     else:
#         return render(request, 'login.html', {'form': LoginForm()})
#
#     return redirect('index')


# def register(request):
#     if request.method == 'POST':
#         form = RegistrationForm(request.POST)
#         if form.is_valid():
#             User.objects.create_user(
#                 username=request.POST['username'],
#                 email=request.POST['email'],
#                 password=request.POST['password']
#             )
#             return redirect('auth:login')
#         else:
#             return render(request, 'register.html', {'form': form})
#     else:
#         return render(
#             request, 'register.html', {'form': RegistrationForm()}
#         )
#
#
# def logout_view(request):
#     logout(request)
#     return redirect('index')
#
#
#
#
#
#
#
# def index(request):
#     return render(request, 'index.html', {'form': TodoForm()})
#

# def todolist(request, todolist_id):
#     todolist = get_object_or_404(TodoList, pk=todolist_id)
#     if request.method == 'POST':
#         redirect('lists:add_todo', todolist_id=todolist_id)
#
#     return render(
#         request, 'todolist.html',
#         {'todolist': todolist, 'form': TodoForm()}
#     )
#
#
# def add_todo(request, todolist_id):
#     if request.method == 'POST':
#         form = TodoForm(request.POST)
#         if form.is_valid():
#             user = request.user if request.user.is_authenticated else None
#             todo = Todo(
#                 description=request.POST['description'],
#                 todolist_id=todolist_id,
#                 creator=user
#             )
#             todo.save()
#             return redirect('lists:todolist', todolist_id=todolist_id)
#         else:
#             return render(request, 'todolist.html', {'form': form})
#
#     return redirect('lists:index')
#
#
# @login_required
# def overview(request):
#     if request.method == 'POST':
#         return redirect('add_todolist')
#     return render(request, 'overview.html', {'form': TodoListForm()})
#
#
# def new_todolist(request):
#     if request.method == 'POST':
#         form = TodoForm(request.POST)
#         if form.is_valid():
#             # create default todolist
#             user = request.user if request.user.is_authenticated else None
#             todolist = TodoList(creator=user)
#             todolist.save()
#             todo = Todo(
#                 description=request.POST['description'],
#                 todolist_id=todolist.id,
#                 creator=user
#             )
#             todo.save()
#             return redirect('todolist', todolist_id=todolist.id)
#         else:
#             return render(request, 'index.html', {'form': form})
#
#     return redirect('index')
#
#
# def add_todolist(request):
#     if request.method == 'POST':
#         form = TodoListForm(request.POST)
#         if form.is_valid():
#             user = request.user if request.user.is_authenticated else None
#             todolist = TodoList(title=request.POST['title'], creator=user)
#             todolist.save()
#             return redirect('todolist', todolist_id=todolist.id)
#         else:
#             return render(request, 'overview.html', {'form': form})
#
#     return redirect('index')
# def index(request):
#     if request.method=="POST":
#         form=TodoForm(request.POST)
#
#
#         if form.is_valid():
#             new_task=form.save(commit=False)
#             new_task.save()
#             return HttpResponseRedirect('/')
#         else:
#             form=TodoForm()
#
#         all_tasks=Todo.objects.all()
#         return render(request,'index.html',{'form':form,'tasks':all_tasks})
# def todo_delete(request,id):
#     task_to_delete=get_object_or_404(Todo,pk=id).delete()
#     return HttpResponseRedirect('/')


class ToDoCreateView(CreateView):
    model = Todo
    fields = '__all__'
    template_name = 'index.html'
    success_url = '/'
class List_todo(CreateView):
    model=TodoList
    fields = '__all__'
    template_name = 'index.html'
    success_url = '/'


def get_context_data(self, **kwargs):
    context = super(DisplayView, self).get_context_data(**kwargs)
    obj = TodoList.objects.all()
    context['obj'] = obj
    return context