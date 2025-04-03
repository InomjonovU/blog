from . import serializers
from main import models
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def get_users(request):
    users = models.CustomUser.objects.all()
    serializer = serializers.CustomUserSerializer(users, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_posts(request):
    posts = models.Post.objects.all()
    serializer = serializers.PostSerializer(posts, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_comments(request):
    comments = models.Comment.objects.all()
    serializer = serializers.CommentSerializer(comments, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_likes(request):
    likes = models.Like.objects.all()
    serializer = serializers.LikeSerializer(likes, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_tags(request):
    tags = models.Tag.objects.all()
    serializer = serializers.TagSerializer(tags, many=True)
    return Response(serializer.data)

