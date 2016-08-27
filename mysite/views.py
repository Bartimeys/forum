from django.shortcuts import render
from .models import Post, Category, Topic
from django.views.generic import View, ListView, DetailView
from django.utils import timezone


class HomeView(ListView):
    model = Category
    template_name = 'forum/home_page.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        # category_id = int(self.kwargs['category_id'])
        categories_model = []
        for category in Category.objects.all():
            topics = Topic.objects.filter(category_id=category.id).all()
            posts_count = 0
            for topic in topics:
                posts = Post.objects.filter(topic_id=topic.id).all()
                posts_count += len(posts)
            len_topic = len(topics)
            categories_model.append({'category': category, 'topics_count': len_topic,
                                     'posts_count': posts_count})
        context['category_model'] = categories_model
        print context
        return context


class CategoryView(ListView):
    model = Topic
    template_name = 'forum/category.html'

    def get_context_data(self, **kwargs):
        context = super(CategoryView, self).get_context_data(**kwargs)
        category_id = int(self.kwargs['category_id'])
        category_model = []
        for topic in Topic.objects.filter(category_id=category_id):
            posts = Post.objects.filter(topic_id=topic.id)
            last_post = posts[posts.count() - 1]
            date_last_post = last_post.date
            len_post_top = len(posts)
            category_model.append({'topic': topic, 'posts_count': len_post_top, 'datetime_last_post': date_last_post})
        context['category_model'] = category_model
        return context


class PostList(ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'forum/topic.html'

    def get_queryset(self):
        topic_id = int(self.kwargs['topic_id'])
        return Post.objects.filter(topic_id=topic_id)
