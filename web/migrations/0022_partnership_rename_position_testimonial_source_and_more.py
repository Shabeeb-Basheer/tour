# Generated by Django 5.0.1 on 2024-09-28 11:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0021_alter_nearplace_sub_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='Partnership',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=180)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=180)),
                ('company_name', models.CharField(max_length=180)),
                ('proposal_description', models.TextField()),
            ],
            options={
                'verbose_name': 'Partnership',
                'verbose_name_plural': 'Partnerships',
                'ordering': ('id',),
            },
        ),
        migrations.RenameField(
            model_name='testimonial',
            old_name='position',
            new_name='source',
        ),
        migrations.RemoveField(
            model_name='hotel',
            name='video_cover_image',
        ),
        migrations.RemoveField(
            model_name='hotel',
            name='video_url',
        ),
        migrations.RemoveField(
            model_name='hotelamenitiescategory',
            name='hotel',
        ),
        migrations.RemoveField(
            model_name='hotelimage',
            name='description',
        ),
        migrations.AddField(
            model_name='client',
            name='hotel',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='web.hotel'),
        ),
        migrations.AddField(
            model_name='event',
            name='point',
            field=models.CharField(blank=True, max_length=180, null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='point_2',
            field=models.CharField(blank=True, max_length=180, null=True),
        ),
        migrations.AddField(
            model_name='hotel',
            name='bathroom_capasity',
            field=models.CharField(blank=True, max_length=180, null=True),
        ),
        migrations.AddField(
            model_name='hotel',
            name='guest_capasity',
            field=models.CharField(blank=True, max_length=180, null=True),
        ),
        migrations.AddField(
            model_name='hotel',
            name='meals',
            field=models.CharField(blank=True, max_length=180, null=True),
        ),
        migrations.AddField(
            model_name='hotel',
            name='room_capacity',
            field=models.CharField(blank=True, max_length=180, null=True),
        ),
        migrations.AddField(
            model_name='hotelamenities',
            name='icon',
            field=models.FileField(blank=True, null=True, upload_to='amenities_icon/'),
        ),
        migrations.AddField(
            model_name='testimonial',
            name='is_active',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='testimonial',
            name='logo',
            field=models.FileField(blank=True, null=True, upload_to='testimonial-logo/'),
        ),
        migrations.AlterField(
            model_name='hotelenquiry',
            name='check_in',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='hotelenquiry',
            name='check_out',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='meta',
            name='page',
            field=models.CharField(choices=[('home', 'Home'), ('about', 'About'), ('hotels', 'Hotels'), ('image_gallery', 'Image Gallery'), ('video_gallery', 'Video Gallery'), ('nearby_place', 'Nearby Place'), ('events', 'Events'), ('updates', 'Updates'), ('contact_us', 'Contact Us')], max_length=20),
        ),
    ]
