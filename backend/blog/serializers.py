from rest_framework import serializers
from django.contrib.auth.models import User, Group
from .models import Post, Tag, Profile


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        tags = TagSerializer(required=False)
        fields = ['id', 'author', 'tags', 'title', 'body', 'published', 'publish_date', 'category', 
                'date_created', 'date_modified', 'meta_description']


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

