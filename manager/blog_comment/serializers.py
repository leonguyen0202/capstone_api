from rest_framework import serializers
from blog_comment.models import BlogComment
from blog_comment_reply.serializers import BlogCommentReplySerializer

class BlogCommentSerializer(serializers.ModelSerializer):
    replies = BlogCommentReplySerializer(many=True, read_only=True)
    class Meta:
        model = BlogComment
        fields = '__all__'