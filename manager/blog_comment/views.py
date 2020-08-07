from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import BlogComment
from .serializers import BlogCommentSerializer
# Create your views here.

class BlogCommentList(APIView):
    def get(self, request):
        pass