from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views import View
from datetime import datetime
from .models import Category, Post, Comment, Teg





class PostListView(View):
    """Вывод статей категорий"""
    def get_queryset(self):
        return Post.objects.filter(published=True, published_date__lte=datetime.now())

    def get(self, request, category_slug=None, slug=None):
        category_list = Category.objects.filter(published=True)
        if category_slug is not None:
            posts = self.get_queryset().filter(category__slug=category_slug, category__published=True)
        elif slug is not None:
            posts = self.get_queryset().filter(tags__slug=slug)
        else:
            posts = self.get_queryset()
        if posts.exists():
            template = posts.first().get_category_template()
        else:
            template = "blog/post_list.html"
        return render(request, template, {'post_list': posts, "categories": category_list})


class PostDetailView(View):
    """Вывод информации статьи"""

    def get(self, request, **kwargs):
        category_list = Category.objects.filter(published=True)
        post = get_object_or_404(Post, slug=kwargs.get("slug"))
        comments = Comment.objects.filter(post=post)
        return render(request, post.template, {"categories": category_list, 'post': post, "comments": comments})