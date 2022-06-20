from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Post


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request=request, template_name='blog/home.html', context=context)


# Use class view instead of home() function view
class PostListView(ListView):
    model = Post
    # By default, Django expects template to be in:
    # <app>/<model>_<viewtype>.html
    # change to existing template:
    template_name = 'blog/home.html'

    context_object_name = 'posts'
    ordering = ['-date_posted']  # sort by newest to oldest


class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def about(request):
    return render(request=request, template_name='blog/about.html', context={'title': 'About'})
