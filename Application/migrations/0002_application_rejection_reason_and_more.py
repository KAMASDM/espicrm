# Generated by Django 4.2 on 2024-05-02 04:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Assessment', '0001_initial'),
        ('Application', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='Rejection_reason',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='application',
            name='application',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Assessment.assessment'),
        ),
    ]
