from .models import Project, Rating_Content
from .serializers import ProjectSerializer, RatingContentSerializer
from rest_framework import viewsets


class ProjectViewSet(viewsets.ModelViewSet):
    """This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class RatingContentViewSet(viewsets.ModelViewSet):
    """This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = Rating_Content.objects.all()
    serializer_class = RatingContentSerializer
