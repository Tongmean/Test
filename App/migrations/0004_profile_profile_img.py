# Generated by Django 4.0.7 on 2022-09-23 02:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0003_remove_profile_profile_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='Profile_Img',
            field=models.ImageField(blank=True, default='Default_User.png', null=True, upload_to=''),
        ),
    ]
