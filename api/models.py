import math
from django.db import models


from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User


class Project(models.Model):
    """Class for project.
    """
    title = models.TextField(max_length=32)
    description = models.TextField(max_length=360)

    def no_of_content_ratings(self):
        """Returns number of ratings of a project. Filter for each project.
        """
        # Include function name in serializers to make it available

        ratings = Rating_Content.objects.filter(project=self)
        return len(ratings)

    def avg_content_rating(self):
        """Returns average number of ratings for each project.
        """
        sum = 0
        ratings = Rating_Content.objects.filter(project=self)
        for rating in ratings:
            sum += rating.stars
        if len(ratings) > 0:
            return math.floor(sum / len(ratings))
        else:
            return 0


class Rating_Content(models.Model):
    """Class for rating project according to its content.
    """
    # reference to project
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    # reference to logged in user that created rating
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    stars = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(10)])

    class Meta:
        """If a person tries to rate the same project, it will be rejected.
        """
        unique_together = (('user', 'project'))
        index_together = (('user', 'project'))


class Rating_Usability(models.Model):
    """Class for rating project according to its usability.
    """
    # reference to project
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    # reference to logged in user that created rating
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    stars = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(10)])

    class Meta:
        """If a person tries to rate the same project, it will be rejected.
        """
        unique_together = (('user', 'project'))
        index_together = (('user', 'project'))
