# Generated by Django 5.0.6 on 2024-07-09 04:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0017_gallery_is_home'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gallery',
            name='is_home',
            field=models.BooleanField(default=False),
        ),
    ]
