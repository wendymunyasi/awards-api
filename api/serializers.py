from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.authtoken.models import Token

from .models import Project, Rating_Content, Rating_Design, Rating_Usability

# Serializers allow complex data such as querysets and model instances to
# be converted to native Python datatypes that can then be easily rendered
# into JSON, XML or other content types. Serializers also provide
# deserialization, allowing parsed data to be converted back into complex
# types, after first validating the incoming data.


class UserSerializer(serializers.ModelSerializer):
    """Serializer to map the User Model instance to the JSON format.
    """
    projects = serializers.StringRelatedField(many=True)

    class Meta:
        """Class to specify the model associated with the serializer (which
        is User model), as well as any additional options such as the
        fields to be included or excluded.
        """
        model = User
        fields = ['id', 'username', 'password', 'projects']
        # fields = ['id', 'username', 'projects', 'password']
        extra_kwargs = {
            'password': {'write_only': True, 'required': True},
            # 'email': {'write_only': True, 'required': True}
        }
        # write_only means we won't be able to see it, hidden from get
        # required for sending

    def create(self, validated_data):
        """This method is already included in the class but I overode it.
        validated data is data coming from the request and has
        already met all the requirements for the model. Now the password will
        be hashed.
        """
        user = User.objects.create_user(**validated_data)
        Token.objects.create(user=user)
        # You can assign a variable to the token and pass it to return
        # to make it available. In this case it is not needed.
        # So we just create it.
        return user


class UserRatingSerializer(serializers.ModelSerializer):
    """Serializer to map the User Model instance to the JSON format.
    """
    class Meta:
        """Class to specify the model associated with the serializer (which
        is User model), as well as any additional options such as the
        fields to be included or excluded.
        """
        model = User
        fields = ['id', 'username']


class ProjectRatingSerializer(serializers.ModelSerializer):
    """Serializer to map the User Model instance to the JSON format.
    """
    owner = UserRatingSerializer()

    class Meta:
        """Class to specify the model associated with the serializer (which
        is User model), as well as any additional options such as the
        fields to be included or excluded.
        """
        model = Project
        fields = ['id', 'title', 'owner']


class ProjectSerializer(serializers.ModelSerializer):
    """Serializer to map the Project Model instance to the JSON format.
    """
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        """Class to specify the model associated with the serializer (which
        is Project model), as well as any additional options such as the
        fields to be included or excluded.
        """
        model = Project
        fields = (
            'id',
            'title',
            'description',
            'no_of_content_ratings',  # function from models same as below
            'avg_content_rating',  # visible through get projects url
            'no_of_usability_ratings',
            'avg_usability_rating',
            'no_of_design_ratings',
            'avg_design_rating',
            'overall_rating',
            'owner',
            'date_created',
            'date_modified',
        )
        read_only_fields = ('date_created', 'date_modified')


class RatingContentSerializer(serializers.ModelSerializer):
    """Serializer to map the Rating_Content Model instance to the JSON format.
    """
    user = UserRatingSerializer()
    project = ProjectRatingSerializer()

    class Meta:
        """Class to specify the model associated with the serializer (which
        is Rating_Content model), as well as any additional options such as
        the fields to be included or excluded.
        """
        model = Rating_Content
        fields = (
            'id',
            'stars',
            'project',
            'user',
            'date_created',
            'date_modified',
        )


class RatingUsabilitySerializer(serializers.ModelSerializer):
    """Serializer to map the Rating_Usability Model instance to JSON format.
    """
    user = UserRatingSerializer()
    project = ProjectRatingSerializer()

    class Meta:
        """Class to specify the model associated with the serializer (which
        is Rating_Usability model), as well as any additional options such as
        the fields to be included or excluded.
        """
        model = Rating_Usability
        fields = (
            'id',
            'stars',
            'project',
            'user',
            'date_created',
            'date_modified',
        )


class RatingDesignSerializer(serializers.ModelSerializer):
    """Serializer to map the Rating_Usability Model instance to JSON format.
    """
    user = UserRatingSerializer()
    project = ProjectRatingSerializer()

    class Meta:
        """Class to specify the model associated with the serializer (which
        is Rating_Design model), as well as any additional options such as
        the fields to be included or excluded.
        """
        model = Rating_Design
        fields = (
            'id',
            'stars',
            'project',
            'user',
            'date_created',
            'date_modified',
        )
