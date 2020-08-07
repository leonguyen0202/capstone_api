from rest_framework import serializers
from .models import BlogCommentReply

class BlogCommentReplySerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogCommentReply
        fields = '__all__'