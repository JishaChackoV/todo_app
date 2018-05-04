from django.db import models
from django.contrib.auth.models import User
# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from django.utils import timezone


# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     email_confirmed = models.BooleanField(default=False)
#
#     @receiver(post_save, sender=User)
#     def update_user_profile(sender, instance, created, **kwargs):
#         if created:
#             Profile.objects.create(user=instance)
#         instance.profile.save()
from django.utils import timezone

class Todo(models.Model):
    task_name = models.CharField(max_length=100,null=True,blank=True)
    creator = models.ForeignKey(User, null=True, related_name='todos', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    finished_at = models.DateTimeField(null=True)
    description = models.CharField(max_length=128,null=True,blank=True)
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
        ordering = ('created_at',)

    def __str__(self):
        return self.title

    def count(self):
        return self.todos.count()

    def count_finished(self):
        return self.todos.filter(is_finished=True).count()

    def count_open(self):
        return self.todos.filter(is_finished=False).count()