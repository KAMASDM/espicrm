# Generated by Django 4.2.9 on 2024-03-27 07:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Master', '0001_initial'),
        ('DetailEnquiry', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='detail_enquiry',
            name='level',
        ),
        migrations.AddField(
            model_name='detail_enquiry',
            name='Current_Education_Details',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Master.edu_level'),
        ),
    ]
