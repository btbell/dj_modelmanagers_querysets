from django.urls import path, include
from . import views

urlpatterns = [
    path('posts', views.posts_list, name='posts_list'),
]