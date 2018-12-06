from rest_framework import serializers
from .models import BlogPost


class BlogPostSerializer(serializers.ModelSerializer):
    """Serializer for the blog post model. Using model serializer as we need the id
    """
    class Meta:
        model = BlogPost
        fields = '__all__'
