from blog.models import Blog
from blog_comment.models import BlogComment
from rest_framework import viewsets, permissions
from blog_comment.serializers import BlogCommentSerializer
from rest_framework.decorators import action
from rest_framework.response import Response

class BlogCommentViewSet(viewsets.ModelViewSet):
    queryset = BlogComment.objects.all()
    # permission_classes = [
    #     permissions.AllowAny
    # ]
    serializer_class = BlogCommentSerializer

    @action(detail=True, methods=["GET"])
    def comments(self, request, slug):
        blog = Blog.objects.first(slug=slug)
        comments = BlogComment.objects.filter(blog_id=blog)
        serializer = BlogCommentSerializer(comments, many=True)
        return Response(serializer.data, status=200)

    @action(detail=True, methods=["POST"])
    def comments(self, request, slug):
        blog = Blog.objects.first(slug=slug)
        data = request.data
        data["blog_id"] = blog.id
        serializer = BlogCommentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.erros, status=400)