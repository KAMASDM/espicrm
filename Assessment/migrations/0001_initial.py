# Generated by Django 4.2 on 2024-03-26 13:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Master', '__first__'),
        ('DetailEnquiry', '__first__'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='assessment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_country', django_countries.fields.CountryField(blank=True, max_length=2, null=True)),
                ('specialisation', models.CharField(blank=True, max_length=100, null=True)),
                ('duration', models.CharField(blank=True, max_length=100, null=True)),
                ('application_fee', models.CharField(blank=True, max_length=100, null=True)),
                ('tution_fee', models.CharField(blank=True, max_length=100, null=True)),
                ('fee_currency', models.CharField(blank=True, max_length=100, null=True)),
                ('course_link', models.CharField(blank=True, max_length=200, null=True)),
                ('notes', models.TextField(blank=True, null=True)),
                ('ass_status', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Master.assessment_status')),
                ('assigned_users', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('course_interested', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Master.course')),
                ('enquiry', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DetailEnquiry.detail_enquiry')),
                ('intake_interested', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Master.intake')),
                ('level_applying_for', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Master.course_levels')),
                ('university', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Master.university')),
            ],
        ),
    ]