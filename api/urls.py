from django.urls import include, path
from rest_framework import routers

from .views import (ProjectViewSet, RatingContentViewSet,
                    RatingUsabilityViewSet, UserViewSet)

router = routers.DefaultRouter()
router.register('projects', ProjectViewSet)
router.register('projects/ratings/content', RatingContentViewSet)
router.register('projects/ratings/usability', RatingUsabilityViewSet)
router.register('users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
