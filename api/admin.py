from django.contrib import admin

# Register your models here.
from .models import Project, Rating_Content, Rating_Design, Rating_Usability

admin.site.register(Project)
admin.site.register(Rating_Content)
admin.site.register(Rating_Usability)
admin.site.register(Rating_Design)
