# Generated by Django 4.2 on 2024-05-30 06:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Master', '0002_alter_enquiryfollowupstatus_user'),
        ('DetailEnquiry', '0002_alter_detail_enquiry_current_education_details'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detail_enquiry',
            name='Current_Education_Details',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Master.edu_level'),
        ),
    ]
