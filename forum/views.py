from .models import Post, Category, Topic
from django.views.generic import ListView,View
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.shortcuts import render, get_object_or_404
from .forms import PostForm
from django.shortcuts import redirect

class HomeView(ListView):
    model = Category
    template_name = 'forum/home_page.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
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

class LoginView(View):
    initial = {'key': 'value'}
    template_name = 'forum/login.html'
    template_name_2 = '/forum/'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        login = request.POST['login']
        request.session['login'] = login
        password = request.POST['password']
        request.session['password'] = password

        return redirect('/forum/')

class PostDetail(ListView):
    model = Post
    template_name = 'forum/post_detail.html'

    def get_context_data(self, **kwargs):
        post_model = []
        post = get_object_or_404(Post)
        context = super(PostDetail, self).get_context_data(**kwargs)
        post_model.append({'post': post})
        print context
        return context
    # return render(request, 'forum/post_detail.html', {'post': post})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            print request.user
            post.save()
            return redirect('forum.views.post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'forum/post_edit.html', {'form': form})


def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('forum.views.post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'forum/post_edit.html', {'form': form})