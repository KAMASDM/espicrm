# Generated by Django 4.2.9 on 2024-03-27 06:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Master', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='enquiry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_First_Name', models.CharField(max_length=100)),
                ('student_Last_Name', models.CharField(max_length=100)),
                ('student_passport', models.CharField(max_length=100)),
                ('student_phone', models.CharField(max_length=10)),
                ('alternate_phone', models.CharField(max_length=10)),
                ('student_email', models.EmailField(max_length=254)),
                ('student_address', models.TextField()),
                ('student_country', django_countries.fields.CountryField(max_length=2)),
                ('student_state', models.CharField(max_length=100)),
                ('student_city', models.CharField(max_length=100)),
                ('student_zip', models.CharField(max_length=10)),
                ('country_interested', django_countries.fields.CountryField(max_length=2)),
                ('notes', models.TextField()),
                ('assigned_users', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('course_interested', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Master.course')),
                ('current_education', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Master.current_education')),
                ('enquiry_status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Master.enquiry_status')),
                ('intake_interested', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Master.intake')),
                ('level_applying_for', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Master.course_levels')),
                ('university_interested', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Master.university')),
            ],
        ),
    ]
