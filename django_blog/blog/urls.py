from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # Home page (you can create an index view)
    path('', views.index if hasattr(views, 'index') else auth_views.LoginView.as_view(template_name='blog/index.html'), name='home'),

    # User Authentication
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='blog/logout.html'), name='logout'),
    path('profile/', views.profile, name='profile'),
]
