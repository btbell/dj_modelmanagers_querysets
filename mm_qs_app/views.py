from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from .models import Post, Author

def posts_list(request):
    all_posts = Post.objects.all()
    admins_posts = Post.objects.get_users_posts('admin')
    context = {
        'all_posts': all_posts,
        'admins_posts': admins_posts
    }
    #messages.info(request, 'Here are all the posts')
    return render(request, 'mm_qs_app/post_list.html', context)
