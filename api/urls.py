from django.urls import path, include
from rest_framework import routers

from .views import ProjectViewSet, RatingContentViewSet, UserViewSet

router = routers.DefaultRouter()
router.register('projects', ProjectViewSet)
router.register('projects/ratings/content', RatingContentViewSet)
router.register('users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
