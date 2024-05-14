# Generated by Django 4.2 on 2024-05-09 12:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Master', '0001_initial'),
        ('Accounts', '0003_alter_payment_payment_mode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='payment_status',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Master.payment_status'),
        ),
    ]