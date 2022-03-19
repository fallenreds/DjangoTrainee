from django.contrib import admin

from .models import Category, Teg, Post, Comment

admin.site.register(Category)
admin.site.register(Teg)
admin.site.register(Post)
admin.site.register(Comment)

