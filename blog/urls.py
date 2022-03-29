from django.urls import path
from . import views

urlpatterns = [
    path('tegs/<slug:slug>',views.TegPostView.as_view(), name="teg_post"),
    path('<slug:category_name>/', views.CategoryView.as_view(), name="category"),
    path('<slug:category>/<slug:slug>', views.PostDetailView.as_view(), name="detail_post"),
    path('', views.HomeView.as_view()),
]
