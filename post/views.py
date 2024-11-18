from django.shortcuts import render, get_object_or_404
from .models import Post

def post_list(request):
    posts = Post.objects.all().order_by('-created')
    return render(request, 'post/postList.html', {'posts': posts})

def post_detail(request, id):
    post = get_object_or_404(Post, id=id)
    return render(request, 'post/postDetail.html', {'post': post})