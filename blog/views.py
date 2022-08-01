from django.shortcuts import render
from django.views import generic
from .models import Post

# Create your views here.

class PostList(generic.ListView):
    model = Post
    querySet = Post.objects.filter(status=1).order_by('-created_by')
    template_name = 'index.html'
    paginate_by = 6


