from rest_framework import serializers
from users.models import Users
from blog.serializers import BlogSerializer

# User Serializers
class UserSerializer(serializers.ModelSerializer):
    blogs = BlogSerializer(many=True, read_only=True)
    class Meta:
        model = Users
        # fields = ['id', 'rmit_id', 'name', 'age', 'email', 'about_me', 'blogs']
        fields = '__all__'