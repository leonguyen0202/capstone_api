from blog.models import Blog
from blog_comment.models import BlogComment
from blog_comment_reply.models import BlogCommentReply
from rest_framework import viewsets, permissions
from blog_comment_reply.serializers import BlogCommentReplySerializer
from rest_framework.decorators import action
from rest_framework.response import Response

class BlogCommentReplyViewSet(viewsets.ModelViewSet):
    queryset = BlogCommentReply.objects.all()
    # permission_classes = [
    #     permissions.AllowAny
    # ]
    serializer_class = BlogCommentReplySerializer

    @action(detail=True, methods=["GET"])
    def replies(self, request, slug, comment):
        blog = Blog.objects.first(slug=slug)
        comments = BlogComment.objects.filter(blog_id=blog)
        replies = BlogCommentReply.objects.filter(comment_id=comments)
        serializer = BlogCommentSerializer(replies, many=True)
        return Response(serializer.data, status=200)

    @action(detail=True, methods=["POST"])
    def replies(self, request, slug, comment):
        blog = Blog.objects.first(slug=slug)
        comment = BlogComment.object.first(id=comment)
        data = request.data
        data["blog_id"] = blog.id
        data["comment_id"] = comment.id
        serializer = BlogCommentReplySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.erros, status=400)