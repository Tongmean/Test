# Generated by Django 4.0.7 on 2022-09-23 01:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ShipmentForm',
            fields=[
                ('Transaction_Number', models.AutoField(primary_key=True, serialize=False)),
                ('Running_num', models.CharField(blank=True, max_length=60, null=True)),
                ('Area', models.CharField(blank=True, choices=[('local', 'local'), ('Oversea', 'Oversea')], max_length=50, null=True)),
                ('FlightNumber', models.CharField(blank=True, max_length=60, null=True)),
                ('ModeOfTranSportation', models.CharField(blank=True, choices=[('Air', 'Air'), ('Truck', 'Truck'), ('Ocean', 'Ocean')], max_length=40, null=True)),
                ('Forwarder', models.CharField(blank=True, max_length=50, null=True)),
                ('ShipperName', models.CharField(blank=True, max_length=70, null=True)),
                ('ShipperCountry', models.CharField(blank=True, max_length=70, null=True)),
                ('CustomDeclarationNumber', models.CharField(blank=True, max_length=70, null=True)),
                ('InvoiceNumber', models.CharField(blank=True, max_length=70, null=True)),
                ('PickTicket', models.CharField(blank=True, max_length=80, null=True)),
                ('BillOfLanding', models.CharField(blank=True, max_length=70, null=True)),
                ('SupplierNAme', models.CharField(blank=True, max_length=70, null=True)),
                ('PartNumber', models.CharField(blank=True, max_length=70, null=True)),
                ('PartDescription', models.CharField(blank=True, max_length=70, null=True)),
                ('InvoiceQuantity', models.CharField(blank=True, max_length=50, null=True)),
                ('InvoiceOUM', models.CharField(blank=True, choices=[('Each', 'Each'), ('Carton', 'Carton'), ('Pail', 'Pail'), ('Piece', 'Piece'), ('Pair', 'Pair'), ('Bottle', 'Bottle')], max_length=70, null=True)),
                ('UnitPrice', models.CharField(blank=True, max_length=50, null=True)),
                ('TotalPackage', models.CharField(blank=True, max_length=50, null=True)),
                ('DateOfIncident', models.DateField(blank=True, max_length=30, null=True)),
                ('TypeOfDiscrepancy', models.CharField(blank=True, choices=[('Shortage Quantity', 'Shortage Quantity'), ('Over Quantity', 'Over Quantity'), ('Wrong Parts', 'Wrong Parts'), ('PO Problem', 'PO Problem')], max_length=40, null=True)),
                ('DetailOfDiscrepancy', models.CharField(blank=True, max_length=70, null=True)),
                ('ShippingDocument', models.FileField(blank=True, null=True, upload_to='ShippingDocument')),
                ('Other', models.FileField(blank=True, null=True, upload_to='OtherDocument')),
                ('SubmitBy', models.CharField(blank=True, max_length=70, null=True)),
                ('SubmitDate', models.DateTimeField(auto_now_add=True, null=True)),
                ('ProcessingTime', models.CharField(blank=True, max_length=70, null=True)),
                ('Status', models.CharField(blank=True, max_length=25, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Fullname', models.CharField(max_length=50, null=True)),
                ('Description', models.CharField(max_length=60, null=True)),
                ('Date_Created', models.DateTimeField(auto_now_add=True, null=True)),
                ('Email', models.EmailField(blank=True, max_length=200, null=True)),
                ('Profile_Img', models.ImageField(blank=True, default='Default_User.png', null=True, upload_to='Profile_pic')),
                ('user', models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='Profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ActionCause',
            fields=[
                ('ActionID', models.AutoField(primary_key=True, serialize=False)),
                ('RootCause', models.CharField(blank=True, max_length=150, null=True)),
                ('Action', models.CharField(blank=True, choices=[('Replace or Return Shipment', 'Replace or Return Shipment'), ('Correct Invoice', 'Correct Invoice'), ('Credit Note', 'Credit Note')], max_length=30, null=True)),
                ('ReferenceDocument', models.FileField(blank=True, null=True, upload_to='ReferenceDocument')),
                ('ReportBy', models.CharField(blank=True, max_length=50, null=True)),
                ('ReportDate', models.DateTimeField(auto_now_add=True, null=True)),
                ('Transaction_Number', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ActionCause', to='App.shipmentform')),
            ],
        ),
    ]
