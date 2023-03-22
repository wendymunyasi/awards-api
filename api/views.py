from .models import Project, Rating_Content, Rating_Usability
from .serializers import ProjectSerializer, RatingContentSerializer, \
    UserSerializer, RatingUsabilitySerializer
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from django.contrib.auth.models import User
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny


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
    permission_classes = [IsAuthenticated]  # unrestricted access

    # The action decorator will route GET requests by default, but may also
    # accept other HTTP methods by setting the methods argument.
    # The decorator allows you to override any viewset-level configuration
    # such as permission_classes, serializer_class, filter_backends.
    # detail=True is 1 specific movie
    # detail=False means list of movies
    @action(detail=True, methods=['POST'])
    def rate_project_content(self, request, pk=None):
        """Rate the content of a project. This updates or creates rating.
        """
        # Ask for data from database
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
                    'message': 'Content rating updated',
                    'result': serializer.data
                }
                return Response(response, status=status.HTTP_200_OK)
            except Exception:
                # If rating doesn't exist for that project then create it
                rating = Rating_Content.objects.create(
                    user=user, project=project, stars=stars)
                serializer = RatingContentSerializer(rating, many=False)
                response = {
                    'message': 'Content rating created',
                    'result': serializer.data
                }
                return Response(response, status=status.HTTP_200_OK)
        else:
            response = {'message': 'You need to provide the ratings for stars'}
            return Response(response, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['POST'])
    def rate_project_usability(self, request, pk=None):
        """Rate the usability of a project.
        """
        # Ask for data from database
        if 'stars' in request.data:
            project = Project.objects.get(id=pk)
            stars = request.data['stars']
            user = request.user
            # print('Xtra info {}'.format(user))
            try:
                # If rating exists for that project then update it
                rating = Rating_Usability.objects.get(
                    user=user.id, project=project.id)
                rating.stars = stars
                rating.save()
                serializer = RatingUsabilitySerializer(rating, many=False)
                response = {
                    'message': 'Usability rating updated',
                    'result': serializer.data
                }
                return Response(response, status=status.HTTP_200_OK)
            except Exception:
                # If rating doesn't exist for that project then create it
                rating = Rating_Usability.objects.create(
                    user=user, project=project, stars=stars)
                serializer = RatingUsabilitySerializer(rating, many=False)
                response = {
                    'message': 'Usability rating created',
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
    permission_classes = [IsAuthenticated]

    def update(self, request, *args, **kwargs):
        """Disables the built in update method that comes with ModelViewSet.
        """
        response = {'message': 'Chill out, ratings cannot be updated like that'}
        return Response(response, status=status.HTTP_400_BAD_REQUEST)

    def create(self, request, *args, **kwargs):
        """Disables the built in create method that comes with ModelViewSet.
        """
        response = {'message': 'Chill out, ratings cannot be created like that'}
        return Response(response, status=status.HTTP_400_BAD_REQUEST)


class RatingUsabilityViewSet(viewsets.ModelViewSet):
    """This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = Rating_Usability.objects.all()
    serializer_class = RatingUsabilitySerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def update(self, request, *args, **kwargs):
        """Disables the built in update method that comes with ModelViewSet.
        """
        response = {'message': 'Chill out, ratings cannot be updated like that'}
        return Response(response, status=status.HTTP_400_BAD_REQUEST)

    def create(self, request, *args, **kwargs):
        """Disables the built in create method that comes with ModelViewSet.
        """
        response = {'message': 'Chill out, ratings cannot be created like that'}
        return Response(response, status=status.HTTP_400_BAD_REQUEST)
