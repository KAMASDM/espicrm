# Generated by Django 4.2.9 on 2024-03-19 09:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Master', '0001_initial'),
        ('Enquiry', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='assessment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_country', django_countries.fields.CountryField(max_length=2)),
                ('specialisation', models.CharField(max_length=100)),
                ('duration', models.CharField(max_length=100)),
                ('application_fee', models.CharField(max_length=100)),
                ('tution_fee', models.CharField(max_length=100)),
                ('fee_currency', models.CharField(max_length=100)),
                ('course_link', models.CharField(max_length=200)),
                ('notes', models.TextField()),
                ('assigned_users', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('course_interested', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Master.course')),
                ('enquiry', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Enquiry.enquiry')),
                ('intake_interested_month', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Master.intake')),
                ('intake_interested_year', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Master.intake_year')),
                ('level_applying_for', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Master.course_levels')),
                ('university', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Master.university')),
            ],
        ),
    ]
