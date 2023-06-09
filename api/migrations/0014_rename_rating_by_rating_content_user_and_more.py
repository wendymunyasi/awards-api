# Generated by Django 4.1.7 on 2023-03-24 08:57

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0013_rename_user_rating_content_rating_by_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rating_content',
            old_name='rating_by',
            new_name='user',
        ),
        migrations.AlterUniqueTogether(
            name='rating_content',
            unique_together={('user', 'project')},
        ),
        migrations.AlterIndexTogether(
            name='rating_content',
            index_together={('user', 'project')},
        ),
    ]
