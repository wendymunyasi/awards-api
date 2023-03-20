from django.db import models


from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User


class Project(models.Model):
    """Class for project.
    """
    title = models.TextField(max_length=32)
    description = models.TextField(max_length=360)


class Rating_Content(models.Model):
    """Class for rating.
    """
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    stars = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(10)])

    class Meta:
        """If a person tries to rate the same project, it will be rejected.
        """
        unique_together = (('user', 'project'))
        index_together = (('user', 'project'))
