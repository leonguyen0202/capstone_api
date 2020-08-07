from rest_framework import serializers
from blog.models import Blog
from blog_comment.serializers import BlogCommentSerializer

# Blog Serializers
class BlogSerializer(serializers.ModelSerializer):
    comments = BlogCommentSerializer(many=True, read_only=True)
    class Meta:
        model = Blog
        fields = '__all__'
        # depth = 1