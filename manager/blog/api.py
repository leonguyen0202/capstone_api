from blog.models import Blog
from rest_framework import viewsets, permissions
from .serializers import BlogSerializer
from rest_framework.decorators import action

class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = BlogSerializer
    lookup_field = 'slug'