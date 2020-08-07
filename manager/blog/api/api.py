from blog.models import *
from rest_framework import viewsets, permissions
from blog.serializers import *
from rest_framework.decorators import action
from rest_framework.response import Response

class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = BlogSerializer
    lookup_field = 'slug'

    # @action(detail=True, methods=["GET"])
    # def comments(self, request, id=None, pk=None):
    #     blog = self.get_object()
    #     # blog_serializer = BlogSerializer(blog)
    #     comments = BlogComment.objects.filter(blog_id=blog)
    #     serializer = BlogCommentSerializer(comments, many=True)
    #     return Response(serializer.data, status=200)

    # @action(detail=True, methods=["POST"])
    # def comment(self, request, id=None):
    #     blog = self.get_object()
    #     data = request.data
    #     data["blog_id"] = blog.id
    #     serializer = BlogCommentSerializer(data=data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=201)
    #     return Response(serializer.erros, status=400)
    #     pass