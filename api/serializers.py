from rest_framework import serializers
from .models import Project, Rating_Content

# Serializers allow complex data such as querysets and model instances to
# be converted to native Python datatypes that can then be easily rendered
# into JSON, XML or other content types. Serializers also provide
# deserialization, allowing parsed data to be converted back into complex
# types, after first validating the incoming data.


class ProjectSerializer(serializers.ModelSerializer):
    """Serializer to map the Project Model instance to the JSON format.
    """

    class Meta:
        """Class to specify the model associated with the serializer (which
        is Project model), as well as any additional options such as the
        fields to be included or excluded.
        """
        model = Project
        fields = ('id', 'title', 'description')


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
