from django.urls import path
from rest_framework import routers
from .views import PostViewSet, UserViewSet, GroupViewSet, links, cv, index


router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'posts', PostViewSet)

urlpatterns = [
    path("", index, name="home"),
    path("links/", links, name="links"),
    path("cv/", cv, name="cv"),
]
