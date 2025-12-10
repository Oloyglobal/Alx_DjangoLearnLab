from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet
from django.urls import path
from .views import feed


router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='post')
router.register(r'comments', CommentViewSet, basename='comment')

urlpatterns = router.urls

urlpatterns = [
    path('feed/', feed, name='feed'),
]
