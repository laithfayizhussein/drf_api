from rest_framework import generics
from .serializer import PostsSerializer
from .models import Posts
from django.db import models
# Create your views here.

class PostsListView(generics.ListCreateAPIView):
    queryset = Posts.objects.all()
    serializer_class = PostsSerializer

class PostsDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Posts.objects.all()
    serializer_class = PostsSerializer

