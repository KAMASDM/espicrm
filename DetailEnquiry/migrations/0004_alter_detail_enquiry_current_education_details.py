# Generated by Django 4.2 on 2024-06-04 06:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Master', '0002_alter_enquiryfollowupstatus_user'),
        ('DetailEnquiry', '0003_alter_detail_enquiry_current_education_details'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detail_enquiry',
            name='Current_Education_Details',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Master.edu_level'),
        ),
    ]