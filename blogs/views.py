from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.decorators import action
from .models import BlogPost
from .serializers import BlogPostSerializer
# Create your views here.


class BlogPostViewSet(viewsets.ModelViewSet):
    """ViewSet for blogpost model"""
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
