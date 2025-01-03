# Generated by Django 5.1.4 on 2024-12-27 16:30

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('campaign', '0002_alter_campaign_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='campaign',
            name='logo',
            field=cloudinary.models.CloudinaryField(max_length=255, null=True, verbose_name='Image'),
        ),
    ]
