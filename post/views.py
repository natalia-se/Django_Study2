from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import RegisterForm
from .models import Post, Profile

def post_list(request):
    posts = Post.objects.all().order_by('-created')
    return render(request, 'post/postList.html', {'posts': posts})

def post_detail(request, id):
    post = get_object_or_404(Post, id=id)
    return render(request, 'post/postDetail.html', {'post': post})

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            # Save profile fields
            profile = Profile.objects.get(user=user)
            profile.profile_pic = form.cleaned_data.get('profile_pic')
            profile.github_link = form.cleaned_data.get('github_link')
            profile.save()
            messages.success(request, 'Your account has been created! You can now log in.')
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'post/register.html', {'form': form})

@login_required
def protected_view(request):
    return render(request, 'welcome.html')