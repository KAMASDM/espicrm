# Generated by Django 4.2.9 on 2024-04-03 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Master', '0009_countryinterested'),
    ]

    operations = [
        migrations.AlterField(
            model_name='countryinterested',
            name='country',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
