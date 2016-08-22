from django.shortcuts import render
from django.utils import timezone
from .models import Post, Category, Topic
from django.http import HttpResponse

def home_page(request):
    categories = Category.objects.all()
    return render(request, 'blog/home_page.html', {'categories': categories})


def category(request, category_id):
    topics = Topic.objects.filter(category_id=category_id)
    # date_last_post = Post.objects.order_by(date__lte=timezone.now()).order_by('date')
    return render(request, 'blog/category.html', {'topics': topics})


def topic(request, topic_id):
    posts = Post.objects.filter(topic_id=topic_id)
    return render(request, 'blog/topic.html', {'posts': posts})


def base(request):
    return render(request, 'blog/base.html', {})
