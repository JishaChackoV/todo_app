from django.http import HttpResponse
from django.views.generic import CreateView
from django.shortcuts import render
from django.views.generic.edit import FormView
from django.contrib.auth import *
from .forms import *
from .models import *


class RegisterUserView(FormView):

        template_name = "To_Do_App/register.html"
        form_class = RegisterUserForm
        success_url = 'To_Do_App/home/'

        def form_valid(self, form):
            # form.save()
            # user.set_password(password)
            get_user_model().objects.create_user(form.cleaned_data.get('email'),
                                                 form.cleaned_data.get('password'),
                                                 form.cleaned_data.get('mobile_no'),
                                                 form.cleaned_data.get('name')
                                                 )

            # messages.success(self.request, "ok")

            return render(self.request, "To_Do_App/home.html")
            # success_url = '/home/'


class LoginUserView(FormView):

        template_name = "To_Do_App/login.html"
        form_class = LoginUserForm

        def post(self, request, *args, **kwargs):
                email = request.POST['email']
                password = request.POST['password']
                # try:
                print(email, password, "dddddddddddddd")
                user = authenticate(request, email=email, password=password)
                print("auth", str(authenticate(email=email, password=password)))

                if user is not None:
                        login(request, user)
                        return render(request, 'To_Do_App/home.html')

                else:
                        return HttpResponse("invalid")


class ToDoCreateView(CreateView):
    model = Todo
    fields = '__all__'
    template_name = 'To_Do_App/index.html'
    success_url = '/'


class List_todo(CreateView):

    model = TodoList
    fields = '__all__'
    template_name = 'To_Do_App/index.html'
    success_url = '/'




def get_context_data(self, **kwargs):
    context = super(DisplayView, self).get_context_data(**kwargs)
    obj = TodoList.objects.all()
    context['obj'] = obj
    return context


