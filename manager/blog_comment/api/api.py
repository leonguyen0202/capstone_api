from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets, permissions
from django.http import HttpResponse

from blog.models import Blog
# from blog.serializers import BlogSerializer
from blog_comment.models import BlogComment
from blog_comment.serializers import BlogCommentSerializer

class BlogCommentViewSet(viewsets.ModelViewSet):
    
    # def list(self, request, slug, comment_id=None):
    #     if comment_id:
    #         comment = BlogComment.objects.filter(id=comment_id)
    #         # appts = Appointment.active.order_by('appt_time').filter(patient=patient)
    #         serializer = BlogCommentSerializer(comment, many=True)
    #         return Response(serializer.data, status=200)
    #     else:
    #         blog = Blog.objects.first(slug=slug)
    #         comments = BlogComment.objects.filter(blog_id=blog.id)
    #         serializer = BlogCommentSerializer(comments, many=True)
    #         return Response(serializer.data, status=200)

    queryset = BlogComment.objects.all()
    # # permission_classes = [
    # #     permissions.AllowAny
    # # ]
    serializer_class = BlogCommentSerializer

    # # @action(detail=True, methods=["GET"])
    # @list_route()
    # def comments(self, request, slug):
    #     blog = Blog.objects.first(slug=slug)
    #     comments = BlogComment.objects.filter(blog_id=blog.id)
    #     serializer = BlogCommentSerializer(comments, many=True)
    #     return Response(serializer.data, status=200)

    # @action(detail=True, methods=["POST"])
    # def comments(self, request, slug):
    #     blog = Blog.objects.first(slug=slug)
    #     data = request.data
    #     data["blog_id"] = blog.id
    #     serializer = BlogCommentSerializer(data=data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=201)
    #     return Response(serializer.erros, status=400)