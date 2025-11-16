from django.contrib import admin
from .models import Book
from django.contrib.auth.admin import UserAdmin
from users.models import CustomUser  # Ensure this points to your CustomUser

# Book admin
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year', 'added_by')
    list_filter = ('author', 'publication_year')
    search_fields = ('title', 'author')

# CustomUser admin
@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('date_of_birth', 'profile_photo')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('date_of_birth', 'profile_photo')}),
    )
    list_display = ['username', 'email', 'first_name', 'last_name', 'date_of_birth', 'is_staff']
