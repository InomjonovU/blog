from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login as auth_login, logout
from .models import *
from django.contrib.auth.decorators import login_required

def main(request):
    return render(request, 'front/index.html', context={'posts': Post.objects.all()}    )

def login(request):
    try:
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            auth_login(request, user)
            return redirect('main:main')
    except Exception as error:
        print(error)
    return render(request, 'front/login.html')

def register(request):
    try:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            email = request.POST.get('email')
            user = CustomUser.objects.create_user(username=username, password=password)
            user.save()
            return redirect('main:profile')
    except Exception as error:
        print(error)
    return render(request, 'front/register.html')

def logout_view(request):
    logout(request)
    return redirect('main:main')

@login_required(login_url='main:login')
def profile(request):
    posts = Post.objects.filter(user=request.user)
    context = {
        'user': request.user,
        'posts': posts,
    }
    return render(request, 'front/profile.html', context)

@login_required(login_url='main:login')
def create_post(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        image = request.FILES['image']
        post = Post.objects.create(user=request.user, title=title, text=content, image=image)
        post.save()
        return redirect('main:profile')
    return render(request, 'front/create_post.html', {'tags': Tag.objects.all()})

@login_required(login_url='main:login')
def post_detail(request, post_id):
    post = Post.objects.get(id=post_id)
    if request.method == 'POST':
        text = request.POST['content']
        Comment.objects.create(post=post, user=request.user, text=text)
    comments = Comment.objects.filter(post=post)
    return render(request, 'front/post_detail.html', {'post': post, 'comments': comments})

@login_required(login_url='main:login')
def user_profile_detail(request, user_id):
    user = get_object_or_404(CustomUser, id=user_id)
    posts = Post.objects.filter(user=user)
    is_following = False

    if request.user.is_authenticated:
        is_following = request.user.following.filter(id=user_id).exists()
    followers_count = user.followers.count()
    following_count = user.following.count()

    context = {
        'user': user,
        'posts': posts,
        'is_following': is_following,
        'followers_count': followers_count,
        'following_count': following_count,
    }
    return render(request, 'front/user_profile_detail.html', context)

@login_required(login_url='main:login')
def users(request):
    users = CustomUser.objects.all()
    search = request.GET.get('search')
    if search:
        users = users.filter(username__icontains=search)
    return render(request, 'front/users.html', {'users': users})

@login_required
def follow_user(request, user_id):
    if request.method == 'POST':
        user_to_follow = get_object_or_404(CustomUser, id=user_id)
        if user_to_follow != request.user:
            request.user.following.add(user_to_follow)
    return redirect('main:user_profile_detail', user_id=user_id)

@login_required
def unfollow_user(request, user_id):
    if request.method == 'POST':
        user_to_unfollow = get_object_or_404(CustomUser, id=user_id)
        request.user.following.remove(user_to_unfollow)
    return redirect('main:user_profile_detail', user_id=user_id)

@login_required(login_url='main:login')
def followers(request):
    followers = request.user.followers.all()
    context = {
        'followers': followers,
        'followers_count': followers.count(),
    }
    return render(request, 'front/followers.html', context)

@login_required(login_url='main:login')
def following(request):
    following = request.user.following.all()
    context = {
        'following': following,
        'following_count': following.count(),
    }
    return render(request, 'front/following.html', context)

@login_required(login_url='main:login')
def user_followers(request, user_id):
    user = get_object_or_404(CustomUser, id=user_id)
    followers = user.followers.all()
    return render(request, 'front/user_followers.html', {'followers': followers})

@login_required(login_url='main:login')
def user_following(request, user_id):
    user = get_object_or_404(CustomUser, id=user_id)
    following = user.following.all()
    return render(request, 'front/user_following.html', {'following': following})

def posts(request):
    subscribed_posts = Post.objects.filter(user__in=request.user.following.all())
    return render(request, 'front/posts.html', {'posts': subscribed_posts})

@login_required(login_url='main:login')
def profile_edit(request):
    try:
        if request.method == 'POST':
            username = request.POST['username']
            email = request.POST['email']
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            bio = request.POST['bio']
            address = request.POST['address']
            website = request.POST['website']
            telegram = request.POST['telegram']
            instagram = request.POST['instagram']
            profile_image = request.FILES['profile_image']
            user = CustomUser.objects.get(id=request.user.id)
            user.username = username
            user.email = email
            user.first_name = first_name
            user.last_name = last_name
            user.bio = bio
            user.address = address
            user.website = website
            user.telegram = telegram
            user.instagram = instagram
            user.profile_image = profile_image
            user.save()
            return redirect('main:profile')
    except Exception as error:
        print(error)
    return render(request, 'front/profile_edit.html', {'user': request.user})

@login_required(login_url='main:login')
def comment(request, post_id):
    post = Post.objects.get(id=post_id)
    if request.method == 'POST':
        text = request.POST['content']
        Comment.objects.create(post=post, user=request.user, text=text)
        return redirect('main:post_detail', post_id=post_id)
    return render(request, 'front/post_detail.html', {'post': post})