# Generated by Django 4.2 on 2024-03-22 07:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Master', '0002_duolingo_exam_edu_level_gmat_exam_gre_exam_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='gre_exam',
            old_name='overall',
            new_name='Overall',
        ),
    ]
