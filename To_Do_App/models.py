from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)


 # Create your models here.
class Todo(models.Model):
    task_name = models.CharField(max_length=100, null=True, blank=True)
    creator = models.ForeignKey(User, null=True, related_name='todos', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    finished_at = models.DateTimeField(null=True)
    description = models.CharField(max_length=128, null=True, blank=True)
    is_finished = models.BooleanField(default=False)

    class Meta:
         ordering = ('created_at',)

    def __str__(self):
        return self.task_name


class TodoList(models.Model):
    title = models.CharField(max_length=128, default='untitled')
    created_at = models.DateTimeField(auto_now=True)
    creator = models.ForeignKey(User, null=True, related_name='todolists', on_delete=models.CASCADE)

    class Meta:
        ordering = ( 'created_at', )

    def __str__(self):
        return self.title

    def count(self):
        return self.todos.count()

    def count_finished(self):
        return self.todos.filter(is_finished=True).count()

    def count_open(self):
        return self.todos.filter(is_finished=False).count()


class MyUserManager(BaseUserManager):
    def create_user(self,email,password=None, mobile_no=None,name=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            mobile_no=mobile_no,
            name=name
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,email,password):
        user=self.create_user(
        email,
        password=password
    )
        user.is_admin=True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50, unique=True)
    mobile_no = models.IntegerField()
    password = models.CharField(max_length=10)

    objects = MyUserManager()
    USERNAME_FIELD = 'email'


