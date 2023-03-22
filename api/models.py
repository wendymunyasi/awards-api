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
        """Returns number of content ratings of a project. Filter for each project.
        """
        # Include function name in serializers to make it available

        ratings = Rating_Content.objects.filter(project=self)
        return len(ratings)

    def avg_content_rating(self):
        """Returns average number of content ratings for each project.
        """
        sum = 0
        ratings = Rating_Content.objects.filter(project=self)
        for rating in ratings:
            sum += rating.stars
        if len(ratings) > 0:
            return math.floor(sum / len(ratings))
        else:
            return 0

    def no_of_usability_ratings(self):
        """Returns number of usability ratings of a project.
        """
        # Include function name in serializers to make it available

        ratings = Rating_Usability.objects.filter(project=self)
        return len(ratings)

    def avg_usability_rating(self):
        """Returns average number of usability ratings for each project.
        """
        sum = 0
        ratings = Rating_Usability.objects.filter(project=self)
        for rating in ratings:
            sum += rating.stars
        if len(ratings) > 0:
            return math.floor(sum / len(ratings))
        else:
            return 0

    def no_of_design_ratings(self):
        """Returns number of design ratings of a project.
        """
        # Include function name in serializers to make it available

        ratings = Rating_Design.objects.filter(project=self)
        return len(ratings)

    def avg_design_rating(self):
        """Returns average number of design ratings for each project.
        """
        sum = 0
        ratings = Rating_Design.objects.filter(project=self)
        for rating in ratings:
            sum += rating.stars
        if len(ratings) > 0:
            return math.floor(sum / len(ratings))
        else:
            return 0

    def overall_rating(self):
        """Returns overall rating of a project
        """
        cont_sum = 0
        desgn_sum = 0
        usab_sum = 0
        content_ratings = Rating_Content.objects.filter(project=self)
        design_ratings = Rating_Design.objects.filter(project=self)
        usability_ratings = Rating_Usability.objects.filter(project=self)
        for rating in content_ratings:
            cont_sum += rating.stars
        for rating in design_ratings:
            desgn_sum += rating.stars
        for rating in usability_ratings:
            usab_sum += rating.stars
        ratings = cont_sum + desgn_sum + usab_sum
        average = ratings / 3
        if ratings > 0:
            return math.floor(average)
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


class Rating_Design(models.Model):
    """Class for rating project according to its design.
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
