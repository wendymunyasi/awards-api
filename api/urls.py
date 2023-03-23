from django.urls import include, path
from rest_framework import routers

from .views import (AllRatingsViewSet, ProjectViewSet, RatingContentViewSet,
                    RatingDesignViewSet, RatingUsabilityViewSet, UserViewSet)

router = routers.DefaultRouter()
router.register('projects', ProjectViewSet)
router.register('projects/ratings/all',
                AllRatingsViewSet, basename='all-ratings')
router.register('projects/ratings/content', RatingContentViewSet)
router.register('projects/ratings/usability', RatingUsabilityViewSet)
router.register('projects/ratings/design', RatingDesignViewSet)
router.register('users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
