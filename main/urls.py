from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.main, name='main'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('create_post/', views.create_post, name='create_post'),
    path('post_detail/<int:post_id>/', views.post_detail, name='post_detail'),
    path('user_profile_detail/<int:user_id>/', views.user_profile_detail, name='user_profile_detail'),
    path('followers/', views.followers, name='followers'),
    path('following/', views.following, name='following'),
    path('users/', views.users, name='users'),
    path('follow/<int:user_id>/', views.follow_user, name='follow_user'),
    path('unfollow/<int:user_id>/', views.unfollow_user, name='unfollow_user'),
    path('user_followers/<int:user_id>/', views.user_followers, name='user_followers'),
    path('user_following/<int:user_id>/', views.user_following, name='user_following'),
    path('posts/', views.posts, name='posts'),
    path('profile_edit/', views.profile_edit, name='profile_edit'),
    # path('post_edit/<int:post_id>/', views.post_edit, name='post_edit'),
    # path('post_delete/<int:post_id>/', views.post_delete, name='post_delete'),
    path('comment/<int:post_id>/', views.comment, name='comment'),
    path('like_or_dislike_post/<int:post_id>/', views.like_or_dislike_post, name='like_or_dislike_post'),
]

