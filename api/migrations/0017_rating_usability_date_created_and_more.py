# Generated by Django 4.1.7 on 2023-03-24 10:08

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0016_rename_rater_rating_content_user_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='rating_usability',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='rating_usability',
            name='date_modified',
            field=models.DateTimeField(auto_now=True),
        ),
    ]