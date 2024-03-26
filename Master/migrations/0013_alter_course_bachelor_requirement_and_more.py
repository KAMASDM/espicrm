# Generated by Django 4.2.9 on 2024-03-22 11:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Master', '0012_alter_university_univ_logo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='bachelor_requirement',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Master.bachelor_requirement'),
        ),
        migrations.AlterField(
            model_name='university',
            name='bachelor_requirement',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Master.bachelor_requirement'),
        ),
    ]
