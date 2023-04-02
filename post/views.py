from django.shortcuts import render
from django.views.generic import DetailView

from post.models import Post


class PostDetailView(DetailView):
    model = Post
