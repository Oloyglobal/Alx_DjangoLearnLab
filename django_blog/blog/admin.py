
# Register your models here.
from django.contrib import admin
from .models import Post, Profile
from .models import Post, Profile, Tag, Comment
from taggit.admin import TaggableAdmin


admin.site.register(Post)
admin.site.register(Profile)
admin.site.register(Tag)
admin.site.register(Comment)



@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "published", "created_at")
    prepopulated_fields = {"slug": ("title",)}
    search_fields = ("title", "content")
