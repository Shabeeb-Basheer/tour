# Generated by Django 5.0.6 on 2024-07-09 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0018_alter_gallery_is_home'),
    ]

    operations = [
        migrations.AddField(
            model_name='nearplace',
            name='offer_price',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='nearplace',
            name='price',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
