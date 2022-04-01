from django.shortcuts import render
from django.views import View
from django.shortcuts import render, get_object_or_404, redirect
from .models import Page

class PageView(View):
    def get(self, request, slug):
        page = Page.objects.get(slug=slug)
        return render(request, 'page/index.html', {"page": page})