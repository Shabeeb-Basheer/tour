# Generated by Django 5.0.6 on 2024-07-05 12:26

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("web", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="banner",
            name="sub_title",
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name="banner",
            name="title",
            field=models.CharField(max_length=40),
        ),
    ]
