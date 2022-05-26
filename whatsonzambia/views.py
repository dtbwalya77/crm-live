from multiprocessing import context
from queue import Empty
from urllib import request
from django import forms
from django.shortcuts import get_object_or_404, render, get_list_or_404
from django.core.paginator import Paginator, EmptyPage
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import(
    ListView, 
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
) 
from .models import Post, PostFeature
from .forms import PostCreateForm, PostFeatureCreateForm
from .models import CustomUser


def home(request):
    if request.method == 'POST':
        day = request.POST['day']
        my_town = request.POST['town']
        posts = Post.objects.filter(event_day=day, town=my_town)
        features = PostFeature.objects.all()
        p = Paginator(posts, 2)
        page_num = request.GET.get('page', 1)

        try:
            page = p.page(page_num)
        except EmptyPage:
            page = p.page(1)

        context = {
            'posts': page,
            'features': features
        }
    else:
        posts = Post.objects.all()
        features = PostFeature.objects.all()
        p = Paginator(posts, 2)
        page_num = request.GET.get('page', 1)

        try:
            page = p.page(page_num)
        except EmptyPage:
            page = p.page(1)

        context = {
            'posts': page,
            'features': features
        }        

    return render(request, 'whatsonzambia/home.html', context)


class PostListView(ListView):
    model = Post
    template_name = 'whatsonzambia/home.html'
    context_object_name = 'posts'
    paginate_by = 2

    def get_context_data(self, **kwargs):
        context = super(PostListView, self).get_context_data(**kwargs)
        context['features'] = PostFeature.objects.all() 
        
        return context


class UserPostListView(ListView):
    model = Post
    template_name = 'whatsonzambia/user_posts.html' #<app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    paginate_by = 2  

    def get_queryset(self):
        user = get_object_or_404(CustomUser, email=self.kwargs.get('email'))
        return Post.objects.filter(author=user).order_by('-date_posted')


class PostDetailView(DetailView):
    model = Post


class PostDetailFeatureView(DetailView):
    model = PostFeature


class PostCreateView(LoginRequiredMixin, CreateView):
    post_image = forms.ImageField()
    model = Post
    template_name = 'whatsonzambia/post_form.html'
    form_class = PostCreateForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostCreateFeatureView(LoginRequiredMixin, CreateView):
    ft_post_image = forms.ImageField()
    model = PostFeature
    template_name = 'whatsonzambia/postfeature_form.html'
    form_class = PostFeatureCreateForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)



class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    post_image = forms.ImageField()
    model = Post
    template_name = 'whatsonzambia/post_form.html'
    form_class = PostCreateForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostUpdateFeatureView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    post_image = forms.ImageField()
    model = Post
    template_name = 'whatsonzambia/postfeature_form.html'
    form_class = PostFeatureCreateForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteFeatureView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = PostFeature
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

def about(request):
    return render(request, 'whatsonzambia/about.html')        