from django.urls import path, include
from rest_framework import routers

from .views import ProjectViewSet, RatingContentViewSet, UserViewSet, \
    RatingUsabilityViewSet

router = routers.DefaultRouter()
router.register('projects', ProjectViewSet)
router.register('projects/ratings/content', RatingContentViewSet)
router.register('projects/ratings/usability', RatingUsabilityViewSet)
router.register('users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
