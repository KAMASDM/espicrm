# Generated by Django 4.2 on 2024-04-26 05:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Master', '0006_paymentfollowupstatus_enquiryfollowupstatus_and_more'),
        ('Accounts', '0004_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='PaymentFollowup',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Master.paymentfollowupstatus'),
        ),
    ]
