# Generated by Django 4.1.7 on 2023-03-23 18:41

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_profile'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='user',
            new_name='owner',
        ),
        migrations.AddField(
            model_name='project',
            name='highlighted',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]