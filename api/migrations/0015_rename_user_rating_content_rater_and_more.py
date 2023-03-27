# Generated by Django 4.1.7 on 2023-03-24 09:22

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0014_rename_rating_by_rating_content_user_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rating_content',
            old_name='user',
            new_name='rater',
        ),
        migrations.AlterUniqueTogether(
            name='rating_content',
            unique_together={('rater', 'project')},
        ),
        migrations.AlterIndexTogether(
            name='rating_content',
            index_together={('rater', 'project')},
        ),
    ]