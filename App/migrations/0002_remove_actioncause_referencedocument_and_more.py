# Generated by Django 4.0.7 on 2022-09-23 01:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='actioncause',
            name='ReferenceDocument',
        ),
        migrations.RemoveField(
            model_name='shipmentform',
            name='Other',
        ),
        migrations.RemoveField(
            model_name='shipmentform',
            name='ShippingDocument',
        ),
    ]
