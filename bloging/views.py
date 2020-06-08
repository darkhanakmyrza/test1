from django.shortcuts import render
from django.core.paginator import Paginator
from django.contrib.auth.models import User
from .models import Post
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import CreateView, UpdateView, DeleteView
# Create your views here.

NUM_OF_POSTS = 5 # Number of post in each page

def home(request, username=None):
    first_name = ''
    last_name = ''
    if username:
        user = User.objects.get(username = username)
        first_name = user.first_name
        last_name = user.last_name
        post_list = Post.objects.filter(user=user)
    else:
        post_list = Post.objects.all()

    post_list = post_list.order_by('-pub_date')
    paginator = Paginator(post_list, NUM_OF_POSTS)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'blog/home.html', {'posts': posts,
                                              'first_name': first_name,
                                              'last_name': last_name} )

def postView(request, pk):
    post = Post.objects.get(pk=pk)
    return render(request, 'blog/post.html', {'post': post})


class PostDelete(DeleteView):
    model = Post
    success_url = reverse_lazy('blog:home')
    template_name = 'blog/post_confirm_delete.html'
    def test_func(self):
        return Post.objects.get(id=self.kwargs['pk']).user == self.request.user


class PostUpdate(UpdateView):
    model = Post
    fields = ['title', 'body', 'img']
    template_name = 'blog/create_post.html'


    def test_func(self):
        return Post.objects.get(id=self.kwargs['pk']).user == self.request.user

class PostCreate(CreateView):
    model = Post
    fields = ['title', 'body', 'img']
    template_name = 'blog/create_post.html'


    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

