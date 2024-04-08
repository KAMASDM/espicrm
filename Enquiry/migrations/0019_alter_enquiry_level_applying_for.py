# Generated by Django 4.2.9 on 2024-04-04 08:32

from django.db import migrations
import django.db.models.deletion
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('Master', '0011_alter_university_country'),
        ('Enquiry', '0018_alter_enquiry_level_applying_for'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enquiry',
            name='level_applying_for',
            field=smart_selects.db_fields.ChainedForeignKey(auto_choose=True, chained_field='course_interested', chained_model_field='course_name', on_delete=django.db.models.deletion.CASCADE, to='Master.course_levels'),
        ),
    ]