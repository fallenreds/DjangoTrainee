from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

from .models import Category, Post


class PostView(View):
    """Вывод постов"""

    def get(self, request):
        post_list = Post.objects.all()
        return render(request, "blog/Post.html", {"posts": post_list})

class HomeView(View):
    """Home page"""

    def get(self, request):
        category_list = Category.objects.all()
        return render(request, "blog/home.html", {"categories": category_list})

class CategoryView(View):
    """Вывод статей категорий"""

    def get(self, request, category_name):
        category= Category.objects.get(slug=category_name)
        return render(request, "blog/post_list.html", {"category": category})
