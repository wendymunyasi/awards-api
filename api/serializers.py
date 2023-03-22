from rest_framework import serializers
from .models import Project, Rating_Content, Rating_Usability
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

# Serializers allow complex data such as querysets and model instances to
# be converted to native Python datatypes that can then be easily rendered
# into JSON, XML or other content types. Serializers also provide
# deserialization, allowing parsed data to be converted back into complex
# types, after first validating the incoming data.


class UserSerializer(serializers.ModelSerializer):
    """Serializer to map the User Model instance to the JSON format.
    """
    # projects = serializers.HyperlinkedRelatedField(
    #     many=True, view_name='project-detail', read_only=True)

    class Meta:
        """Class to specify the model associated with the serializer (which
        is User model), as well as any additional options such as the
        fields to be included or excluded.
        """
        model = User
        fields = ['id', 'username', 'password']
        # fields = ['id', 'username', 'projects', 'password']
        extra_kwargs = {
            'password': {'write_only': True, 'required': True},
            # 'email': {'write_only': True, 'required': True}
        }
        # write_only means we won't be able to see it

    def create(self, validated_data):
        """This method is already included in the class but I overode it.
        validated data is data coming from the request and has
        already met all the requirements for the model.
        """
        user = User.objects.create_user(**validated_data)
        Token.objects.create(user=user)
        # You can assign a variable to the token and pass it to return
        # to make it available. In this case it is not needed.
        # So we just create it.
        return user


class ProjectSerializer(serializers.ModelSerializer):
    """Serializer to map the Project Model instance to the JSON format.
    """

    class Meta:
        """Class to specify the model associated with the serializer (which
        is Project model), as well as any additional options such as the
        fields to be included or excluded.
        """
        model = Project
        fields = ('id', 'title', 'description', 'no_of_content_ratings',
                  'avg_content_rating')


class RatingContentSerializer(serializers.ModelSerializer):
    """Serializer to map the Rating_Content Model instance to the JSON format.
    """
    class Meta:
        """Class to specify the model associated with the serializer (which
        is Rating_Content model), as well as any additional options such as
        the
        fields to be included or excluded.
        """
        model = Rating_Content
        fields = ('id', 'stars', 'project', 'user')


class RatingUsabilitySerializer(serializers.ModelSerializer):
    """Serializer to map the Rating_Usability Model instance to the JSON format.
    """
    class Meta:
        """Class to specify the model associated with the serializer (which
        is Rating_Usability model), as well as any additional options such as
        the
        fields to be included or excluded.
        """
        model = Rating_Usability
        fields = ('id', 'stars', 'project', 'user')
