from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from datetime import datetime
from .models import Category, Post, Comment

class HomeView(View):
    """Home page"""

    def get(self, request):
        category_list = Category.objects.all()
        post_list = Post.objects.filter(published=True, published_date__lte = datetime.now())
        return render(request, "blog/post_list.html", {"categories": category_list, 'post_list': post_list})

class PostDetailView(View):
    """Вывод информации статьи"""

    def get(self, request, slug, category):
        category_list = Category.objects.all()
        post = Post.objects.get(slug=slug)
        comments = Comment.objects.filter(post=post)
        return render(request, post.template, {"categories": category_list, 'post': post, "comments": comments})

class CategoryView(View):
    """Вывод статей категорий"""

    def get(self, request, category_name):
        category= Category.objects.get(slug=category_name)
        return render(request, "blog/post_list.html", {"category": category})

