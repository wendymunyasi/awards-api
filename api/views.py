from .models import Project, Rating_Content
from .serializers import ProjectSerializer, RatingContentSerializer, \
    UserSerializer
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from django.contrib.auth.models import User
from rest_framework.authentication import TokenAuthentication


class UserViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ProjectViewSet(viewsets.ModelViewSet):
    """This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    authentication_classes = [TokenAuthentication]

    # The action decorator will route GET requests by default, but may also
    # accept other HTTP methods by setting the methods argument.
    # The decorator allows you to override any viewset-level configuration
    # such as permission_classes, serializer_class, filter_backends.
    # detail=True is 1 specific movie
    # detail=False means list of movies
    @action(detail=True, methods=['POST'])
    def rate_project_content(self, request, pk=None):
        """Rate the content of a project.
        """
        if 'stars' in request.data:
            project = Project.objects.get(id=pk)
            stars = request.data['stars']
            user = request.user
            # print('Xtra info {}'.format(user))
            try:
                # If rating exists for that project then update it
                rating = Rating_Content.objects.get(
                    user=user.id, project=project.id)
                rating.stars = stars
                rating.save()
                serializer = RatingContentSerializer(rating, many=False)
                response = {
                    'message': 'Rating updated',
                    'result': serializer.data
                }
                return Response(response, status=status.HTTP_200_OK)
            except Exception:
                # If rating doesn't exist for that project then create it
                rating = Rating_Content.objects.create(
                    user=user, project=project, stars=stars)
                serializer = RatingContentSerializer(rating, many=False)
                response = {
                    'message': 'Rating created',
                    'result': serializer.data
                }
                return Response(response, status=status.HTTP_200_OK)
        else:
            response = {'message': 'You need to provide the ratings for stars'}
            return Response(response, status=status.HTTP_400_BAD_REQUEST)


class RatingContentViewSet(viewsets.ModelViewSet):
    """This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = Rating_Content.objects.all()
    serializer_class = RatingContentSerializer
    authentication_classes = [TokenAuthentication]
