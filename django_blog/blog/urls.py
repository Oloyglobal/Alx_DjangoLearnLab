from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # Home page
    path('', views.index if hasattr(views, 'index') else auth_views.LoginView.as_view(template_name='blog/index.html'), name='home'),

    # User Authentication
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='blog/logout.html'), name='logout'),
    path('profile/', views.profile, name='profile'),

    # Blog Post CRUD
    path('posts/', views.PostListView.as_view(), name='post-list'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),
    path('post/new/', views.PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', views.PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post-delete'),

    # Comment URLs (ALX REQUIRED STRUCTURE)
    path('posts/<int:pk>/comments/new/', views.add_comment, name='add_comment'),
    path('comment/<int:pk>/update/', views.edit_comment, name='edit_comment'),
    path('comment/<int:pk>/delete/', views.delete_comment, name='delete_comment'),
]
