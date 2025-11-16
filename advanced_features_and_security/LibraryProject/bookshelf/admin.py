from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Book, CustomUser

# Register Book model
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')
    list_filter = ('author', 'publication_year')
    search_fields = ('title', 'author')

# Register CustomUser model
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    fieldsets = UserAdmin.fieldsets + (
        (None, {"fields": ("date_of_birth", "profile_photo")}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {"fields": ("date_of_birth", "profile_photo")}),
    )
    list_display = ["username", "email", "first_name", "last_name", "date_of_birth", "is_staff"]

admin.site.register(CustomUser, CustomUserAdmin)
