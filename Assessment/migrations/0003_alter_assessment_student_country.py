# Generated by Django 4.2 on 2024-05-03 07:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Master', '0001_initial'),
        ('Assessment', '0002_alter_assessment_assigned_users_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assessment',
            name='student_country',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Master.countryinterested'),
        ),
    ]
