# Generated by Django 4.2 on 2024-05-13 04:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DetailEnquiry', '0002_alter_detail_enquiry_confirmed_services_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detail_enquiry',
            name='Twelveth_Document',
            field=models.FileField(blank=True, upload_to='documents/'),
        ),
    ]