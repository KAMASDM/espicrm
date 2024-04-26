# Generated by Django 4.2 on 2024-04-26 04:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Master', '0006_paymentfollowupstatus_enquiryfollowupstatus_and_more'),
        ('DetailEnquiry', '0005_alter_detail_enquiry_current_enquiry'),
    ]

    operations = [
        migrations.AddField(
            model_name='detail_enquiry',
            name='DetaiEnquiryFollowup',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Master.detailenquiryfollowupstatus'),
        ),
    ]
