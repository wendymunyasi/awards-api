from django.urls import path, include
from rest_framework import routers

from .views import ProjectViewSet, RatingContentViewSet

router = routers.DefaultRouter()
router.register('projects', ProjectViewSet)
router.register('ratings', RatingContentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
