from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm, LoginForm, BlogPostForm
from .models import CustomUser, BlogPost

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('dashboard')
    else:
        form = CustomUserCreationForm()
    return render(request, 'signup.html', {'form': form})

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = CustomUser.objects.filter(username=username).first()
            if user and user.check_password(password):
                auth_login(request, user)
                return redirect('dashboard')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

@login_required
def dashboard(request):
    return render(request, 'dashboard.html', {'user': request.user})

def logout(request):
    auth_logout(request)
    return redirect('login')


@login_required
def create_blog_post(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            blog_post = form.save(commit=False)
            blog_post.author = request.user
            blog_post.save()
            return redirect('myapp:my_blog_posts')
    else:
        form = BlogPostForm()
    return render(request, 'create_blog_post.html', {'form': form})

@login_required
def my_blog_posts(request):
    blog_posts = BlogPost.objects.filter(author=request.user)
    return render(request, 'my_blog_posts.html', {'blog_posts': blog_posts})

def blog_list(request):
    blog_posts = BlogPost.objects.filter(is_draft=False)
    return render(request, 'blog_list.html', {'blog_posts': blog_posts})

def blog_detail(request, pk):
    blog_post = get_object_or_404(BlogPost, pk=pk)
    return render(request, 'blog_detail.html', {'blog_post': blog_post})
