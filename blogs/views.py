from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import BlogPost
from .serializers import BlogPostSerializer, BlogPostListSerializer
# Create your views here.


class BlogPostViewSet(viewsets.ModelViewSet):
    """ViewSet for blogpost model"""
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer

    def list(self, request):
        queryset = BlogPost.objects.all()[:5]
        serializer = BlogPostListSerializer(queryset, many=True)
        return Response(serializer.data)
