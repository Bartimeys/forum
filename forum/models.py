from django.db import models
from django.utils import timezone


class Category(models.Model):
    title = models.CharField(verbose_name='Title', max_length=200)

    def __str__(self):
        return str(self.title)


class Topic(models.Model):
    title = models.CharField(verbose_name='Title', max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.title)


class Post(models.Model):
    user = models.ForeignKey('auth.User')
    title = models.CharField(verbose_name='Title', max_length=200)
    body = models.TextField()
    date = models.DateTimeField(default=timezone.now)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class UserEvent(models.Model):
    user_name = models.CharField(max_length=255, blank=True, null=True)
    login = models.CharField(max_length=255, blank=True, null=True)
    password = models.CharField(max_length=255, blank=True, null=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)