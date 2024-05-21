# Generated by Django 4.2 on 2024-05-21 11:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields
import smart_selects.db_fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Master', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='enquiry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_First_Name', models.CharField(max_length=100)),
                ('student_Last_Name', models.CharField(max_length=100)),
                ('student_passport', models.CharField(max_length=100)),
                ('student_phone', models.CharField(max_length=100)),
                ('alternate_phone', models.CharField(max_length=100)),
                ('student_email', models.EmailField(max_length=254)),
                ('student_address', models.TextField()),
                ('student_country', django_countries.fields.CountryField(default='IN', max_length=2)),
                ('student_state', models.CharField(max_length=100)),
                ('student_city', models.CharField(max_length=100)),
                ('student_zip', models.CharField(max_length=10)),
                ('notes', models.TextField()),
                ('EnquiryFollowup', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Master.enquiryfollowupstatus')),
                ('Interested_Services', models.ManyToManyField(blank=True, default='Counselling', related_name='Interested_Services', to='Master.available_services')),
                ('Source_Enquiry', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Master.enquiry_source')),
                ('assigned_users', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('country_interested', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Master.countryinterested')),
                ('course_interested', smart_selects.db_fields.ChainedForeignKey(auto_choose=True, blank=True, chained_field='university_interested', chained_model_field='university', null=True, on_delete=django.db.models.deletion.CASCADE, to='Master.course')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('current_education', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Master.current_education')),
                ('enquiry_status', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Master.enquiry_status')),
                ('intake_interested', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Master.intake')),
                ('level_applying_for', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Master.course_levels')),
                ('university_interested', smart_selects.db_fields.ChainedForeignKey(auto_choose=True, blank=True, chained_field='country_interested', chained_model_field='country', null=True, on_delete=django.db.models.deletion.CASCADE, to='Master.university')),
            ],
        ),
    ]
