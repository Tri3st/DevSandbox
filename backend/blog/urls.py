from django.urls import path
from . import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'posts', views.PostViewSet)

urlpatterns = [
    path("", views.index, name="home"),
    path("links/", views.links, name="links"),
    path("cv/", views.cv, name="cv"),

    path("api/posts/", views.post_list, name="post_list"),
    path("api/posts/<int:pk>", views.post_detail, name="post_detail"),
]
