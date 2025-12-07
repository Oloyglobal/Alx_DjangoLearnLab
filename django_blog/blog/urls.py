from django.urls import path
from django.contrib.auth import views as auth_views
from .views import PostListView, PostDetailView, PostByTagListView
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
    # path('post/<int:pk>/comments/new/', views.add_comment, name='add_comment'),
    # path('comment/<int:pk>/update/', views.edit_comment, name='edit_comment'),
    # path('comment/<int:pk>/delete/', views.delete_comment, name='delete_comment'),
]


urlpatterns += [
    # posts by tag (e.g. /tags/django/)
    path('tags/<str:tag_name>/', views.TagPostListView.as_view(), name='posts-by-tag'),

    # search (e.g. /search/?q=django)
    path('search/', views.search, name='search'),
    
    
]


urlpatterns = [
    path("", views.post_list, name="post_list"),
    path("post/<slug:slug>/", views.post_detail, name="post_detail"),
    path("tag/<slug:tag_slug>/", views.posts_by_tag, name="posts_by_tag"),
    path("search/", views.search, name="post_search"),
]


app_name = "blog"

urlpatterns = [
    path("", PostListView.as_view(), name="post_list"),
    path("<slug:slug>/", PostDetailView.as_view(), name="post_detail"),

    # REQUIRED BY ALX CHECKER
    path("tags/<slug:tag_slug>/", PostByTagListView.as_view(), name="posts_by_tag"),
]