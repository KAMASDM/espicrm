# Generated by Django 4.2 on 2024-04-06 11:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Assessment', '0001_initial'),
        ('Master', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='assessment',
            name='ass_status',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Master.assessment_status'),
        ),
    ]