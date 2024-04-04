# Generated by Django 4.2.9 on 2024-03-27 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Master', '0002_available_services'),
        ('Enquiry', '0005_alter_enquiry_country_interested'),
    ]

    operations = [
        migrations.AddField(
            model_name='enquiry',
            name='Interested_Services',
            field=models.ManyToManyField(blank=True, default='Consultation', related_name='Interested_Services', to='Master.available_services'),
        ),
    ]
