from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import Group, User
from django.contrib.auth.decorators import login_required
from rest_framework import permissions, viewsets

from .models import Link, Post
from .serializers import PostSerializer, GroupSerializer, UserSerializer



# Create your views here.
def index(request):
    user = request.user
    context = {
        'user': user,
    }
    return render(request, "blog/index.html", context)


@login_required
def links(request):
    user = request.user
    mylinks = Link.objects.all().order_by('name')
    context = {
        'user': user,
        'links': mylinks,
    }
    return render(request, "blog/links.html", context)


@login_required
def cv(request):
    # TODO implement
    user = request.user
    context = {
        'user': user,
    }
    return render(request, "blog/cv.html", context)


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('date_created')
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all().order_by('name')
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

