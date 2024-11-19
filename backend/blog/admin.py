from django.contrib import admin
from blog.models import Post, Profile, Tag, Link

# Register your models here.
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    model = Profile

@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
    model = Link

    list_display = ("name", "url", "description")
    ordering = ("name",)
    list_filter = ("name",)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    model = Tag


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    model = Post

    list_display = (
        "id",
        "title",
        "category",
        "slug",
        "publish_date",
        "published",
    )

    list_filter = (
        "published",
        "publish_date",
    )

    list_editable = (
        "title",
        "category",
        "slug",
        "publish_date",
        "published",
    )

    search_fields = (
        "title",
        "category",
        "slug",
        "body",
    )

    prepoulated_fields = {
        "slug": ("title",
                 "category",
                ),
    }
    date_hierarchy = "publish_date"
    save_on_top = True

