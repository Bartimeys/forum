from django.shortcuts import render
from django.utils import timezone
from .models import Post, Category, Topic
from django.http import HttpResponse


def home_page(request):
    categories = Category.objects.all()
    categories_model = []
    for category in categories:
        topics = Topic.objects.filter(category_id=category.id).all()
        posts_count = 0
        for topic in topics:
            posts = Post.objects.filter(topic_id=topic.id).all()
            posts_count += len(posts)
        len_topic = len(topics)
        categories_model.append({'category': category, 'topics_count': len_topic,
                                 'posts_count' : posts_count})
    return render(request, 'blog/home_page.html', {'categories': categories_model})


def category(request, category_id):
    topics = Topic.objects.filter(category_id=category_id)
    cat_f_top_model = []
    for topic in topics:
        posts = Post.objects.filter(topic_id=topic.id).all()
        last_post = Post.objects.all()[Post.objects.count() - 1]
        date_last_post = last_post.date
        len_post_top = len(posts)
        cat_f_top_model.append({'topic': topic, 'posts_count': len_post_top, 'datetime_last_post': date_last_post})
    return render(request, 'blog/category.html', {'topics': cat_f_top_model})


def topic(request, category_id, topic_id):
    posts = Post.objects.filter(topic_id=topic_id)
    return render(request, 'blog/topic.html', {'posts': posts})


def base(request):
    return render(request, 'blog/base.html', {})
