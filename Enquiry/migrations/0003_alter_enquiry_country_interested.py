# Generated by Django 4.2.9 on 2024-03-27 06:10

from django.db import migrations
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('Enquiry', '0002_alter_enquiry_student_country'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enquiry',
            name='country_interested',
            field=django_countries.fields.CountryField(default='UK', max_length=2),
        ),
    ]
