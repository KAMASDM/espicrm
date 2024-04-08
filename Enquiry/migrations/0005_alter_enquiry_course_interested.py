# Generated by Django 4.2 on 2024-04-06 12:20

from django.db import migrations
import django.db.models.deletion
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('Master', '0003_alter_university_country'),
        ('Enquiry', '0004_alter_enquiry_source_enquiry'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enquiry',
            name='course_interested',
            field=smart_selects.db_fields.ChainedForeignKey(auto_choose=True, blank=True, chained_field='university_interested', chained_model_field='university', null=True, on_delete=django.db.models.deletion.CASCADE, to='Master.course'),
        ),
    ]