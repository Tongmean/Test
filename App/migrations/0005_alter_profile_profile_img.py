# Generated by Django 4.0 on 2023-08-03 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0004_profile_profile_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='Profile_Img',
            field=models.ImageField(blank=True, null=True, upload_to='/'),
        ),
    ]
