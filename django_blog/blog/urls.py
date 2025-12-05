# blog/urls.py
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # Registration
    path('register/', views.register, name='register'),

    # Login (uses built-in view)
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),

    # Logout (uses built-in view)
    path('logout/', auth_views.LogoutView.as_view(template_name='blog/logout.html'), name='logout'),

    # Profile (requires login)
    path('profile/', views.profile, name='profile'),
]




# django_blog/urls.py
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),    # routes for auth + others
    # Optionally map home page to a simple view or TemplateView
    path('', TemplateView.as_view(template_name='blog/index.html'), name='home'),
]

# blog/urls.py
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.index if hasattr(views, 'index') else auth_views.LoginView.as_view(template_name='blog/index.html'), name='home'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='blog/logout.html'), name='logout'),
    path('profile/', views.profile, name='profile'),
]
