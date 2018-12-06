from rest_framework import serializers
from .models import BlogPost


class BlogPostSerializer(serializers.ModelSerializer):
    """Serializer for the blog post model. Using model serializer as we need the id
    """
    class Meta:
        model = BlogPost
        fields = '__all__'


class BlogPostListSerializer(serializers.HyperlinkedModelSerializer):
    """Exlclude the body for list view"""
    id = serializers.ReadOnlyField()

    class Meta:
        model = BlogPost
        exclude = ('body',)
        lookup_field = 'slug'
        extra_kwargs = {
            'url': {'lookup_field': 'slug'}
        }
