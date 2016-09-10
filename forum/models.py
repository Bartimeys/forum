from django.db import models
from django.utils import timezone
from django.core.urlresolvers import reverse


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

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title
