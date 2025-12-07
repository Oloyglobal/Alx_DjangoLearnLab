from django.contrib import admin
from .models import Post, Profile, Tag, Comment

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "published", "created_at")
    prepopulated_fields = {"slug": ("title",)}
    search_fields = ("title", "content")

admin.site.register(Profile)
admin.site.register(Tag)
admin.site.register(Comment)
