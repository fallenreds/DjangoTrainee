from django.urls import path
from . import views

urlpatterns = [
    path('post/', views.PostView.as_view(), name="Post"),
    path('<slug:category_name>/', views.CategoryView.as_view(), name="category"),
    path('', views.HomeView.as_view()),
]
