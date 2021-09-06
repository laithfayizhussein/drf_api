from rest_framework import serializers

from .models import Posts

class PostsSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'body', 'title', 'created_at', 'author')
        model = Posts