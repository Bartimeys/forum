from django.shortcuts import render
from .models import Post, Category, Topic
from django.views.generic import View, ListView


class HomeView(View):

    def get(self, request):
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
                                     'posts_count': posts_count})
        return render(request, 'forum/home_page.html', {'categories': categories_model})

class CategoryView(View):

    def get(self, request, category_id):
        category_id = int(category_id)

        model = Topic.objects.filter(category_id=category_id)
        cat_f_top_model = []
        for topic in model:
            posts = Post.objects.filter(topic_id=topic.id).all()
            last_post = Post.objects.all()[Post.objects.count() - 1]
            date_last_post = last_post.date
            len_post_top = len(posts)
            cat_f_top_model.append({'topic': topic, 'posts_count': len_post_top, 'datetime_last_post': date_last_post})

        return render(request, 'forum/category.html', {'topics': cat_f_top_model})

class PostList(ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'forum/topic.html'

    def get_queryset(self):
        topic_id = int(self.kwargs['topic_id'])
        return Post.objects.filter(topic_id=topic_id)