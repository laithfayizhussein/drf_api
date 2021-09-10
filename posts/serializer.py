from rest_framework import serializers
from .models import Posts

class PostsSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'author', 'title', 'created_at', 'updated_at')
        model = Posts