from django.contrib.auth.models import User
from rest_framework import status, viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from .models import Project, Rating_Content, Rating_Design, Rating_Usability
from .serializers import (ProjectSerializer, RatingContentSerializer,
                          RatingDesignSerializer, RatingUsabilitySerializer,
                          UserSerializer)


class UserViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]


class ProjectViewSet(viewsets.ModelViewSet):
    """This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        """The perform_create method is called by the CreateModelMixin when
        a new project instance is created. By default, it simply calls
        serializer.save() to create the new instance. However, we can
        override this method to include additional logic. In this case,
        we're setting the owner field of the new Project instance to be the
        currently logged in user (self.request.user).
        """
        serializer.save(owner=self.request.user)

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

    @action(detail=True, methods=['POST'])
    def rate_project_design(self, request, pk=None):
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
                rating = Rating_Design.objects.get(
                    user=user.id, project=project.id)
                rating.stars = stars
                rating.save()
                serializer = RatingDesignSerializer(rating, many=False)
                response = {
                    'message': 'Design rating updated',
                    'result': serializer.data
                }
                return Response(response, status=status.HTTP_200_OK)
            except Exception:
                # If rating doesn't exist for that project then create it
                rating = Rating_Design.objects.create(
                    user=user, project=project, stars=stars)
                serializer = RatingDesignSerializer(rating, many=False)
                response = {
                    'message': 'Design rating created',
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

    def list(self, request, *args, **kwargs):
        """Retrieves the data, serializes it, and returns it along with the
        custom text message.
        """
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        response_data = {
            'message': 'List of content ratings',
            'data': serializer.data
        }
        return Response(response_data)

    def update(self, request, *args, **kwargs):
        """Disables the built in update method that comes with ModelViewSet.
        """
        response = {'message': 'Chill out, cannot update ratings like that'}
        return Response(response, status=status.HTTP_400_BAD_REQUEST)

    def create(self, request, *args, **kwargs):
        """Disables the built in create method that comes with ModelViewSet.
        """
        response = {'message': 'Chill out, cannot create ratings like that'}
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
        response = {'message': 'Chill out, cannot update ratings like that'}
        return Response(response, status=status.HTTP_400_BAD_REQUEST)

    def create(self, request, *args, **kwargs):
        """Disables the built in create method that comes with ModelViewSet.
        """
        response = {'message': 'Chill out, cannot create ratings like that'}
        return Response(response, status=status.HTTP_400_BAD_REQUEST)


class RatingDesignViewSet(viewsets.ModelViewSet):
    """This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = Rating_Design.objects.all()
    serializer_class = RatingDesignSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def update(self, request, *args, **kwargs):
        """Disables the built in update method that comes with ModelViewSet.
        """
        response = {'message': 'Chill out, cannot update ratings like that'}
        return Response(response, status=status.HTTP_400_BAD_REQUEST)

    def create(self, request, *args, **kwargs):
        """Disables the built in create method that comes with ModelViewSet.
        """
        response = {'message': 'Chill out, cannot create ratings like that'}
        return Response(response, status=status.HTTP_400_BAD_REQUEST)


class AllRatingsViewSet(viewsets.ReadOnlyModelViewSet):
    """
    A viewset that retrieves all ratings from all rating types.
    """
    serializer_class = None
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def list(self, request):
        """Fetches all ratings from all three models and serializes the data
        using their respective serializers.
        """
        # Retrieve all ratings from all rating types
        content_ratings = Rating_Content.objects.all()
        design_ratings = Rating_Design.objects.all()
        usability_ratings = Rating_Usability.objects.all()

        # Serialize the rating objects using the appropriate serializer
        content_data = RatingContentSerializer(content_ratings, many=True).data
        design_data = RatingDesignSerializer(design_ratings, many=True).data
        usability_data = RatingUsabilitySerializer(
            usability_ratings, many=True).data

        # Combine the serialized data into a single response
        data = {
            'Content Ratings': content_data,
            'Design Ratings': design_data,
            'Usability Ratings': usability_data
        }

        return Response(data)
