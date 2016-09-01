from django import forms
from .models import Post, Category, Topic


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'body','topic')