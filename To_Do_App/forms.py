from  django import forms
import To_Do_App
from .models import *

class RegisterUserForm(forms.ModelForm):
    name = forms.CharField(max_length=10)
    email = forms.EmailField(max_length=50)
    mobile_no = forms.IntegerField()
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
            model = User
            fields = ['name', 'email', 'mobile_no', 'password']


class LoginUserForm(forms.Form):
        email = forms.EmailField(max_length=50)
        password = forms.CharField(widget=forms.PasswordInput)


class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = '__all__'


class TodoForm(forms.ModelForm):
    class Meta:
        model = TodoList
        fields = '__all__'


def __init__(self, args, *kwargs):
    super(TodoForm, self).__init__(*args, **kwargs)
    for field in self.fields.values():
        field.widget.attrs = {'class': 'form-control'}

