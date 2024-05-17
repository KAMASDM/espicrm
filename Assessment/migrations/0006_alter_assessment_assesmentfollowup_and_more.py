# Generated by Django 4.2 on 2024-05-17 09:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('DetailEnquiry', '0003_alter_detail_enquiry_twelveth_document'),
        ('Master', '0005_alter_detailenquiryfollowupstatus_user'),
        ('Assessment', '0005_alter_assessment_assesmentfollowup'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assessment',
            name='AssesmentFollowup',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, to='Master.assesmentfollowupstatus'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='assessment',
            name='application_fee',
            field=models.CharField(blank=True, default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='assessment',
            name='ass_status',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, to='Master.assessment_status'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='assessment',
            name='assigned_users',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='assessment',
            name='course_interested',
            field=smart_selects.db_fields.ChainedForeignKey(auto_choose=True, blank=True, chained_field='university', chained_model_field='university', default=1, on_delete=django.db.models.deletion.CASCADE, to='Master.course'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='assessment',
            name='course_link',
            field=models.CharField(blank=True, default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='assessment',
            name='duration',
            field=models.CharField(blank=True, default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='assessment',
            name='enquiry',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, to='DetailEnquiry.detail_enquiry'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='assessment',
            name='fee_currency',
            field=models.CharField(blank=True, default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='assessment',
            name='intake_interested',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, to='Master.intake'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='assessment',
            name='level_applying_for',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, to='Master.course_levels'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='assessment',
            name='notes',
            field=models.TextField(blank=True, default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='assessment',
            name='specialisation',
            field=models.CharField(blank=True, default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='assessment',
            name='student_country',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, to='Master.countryinterested'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='assessment',
            name='tution_fee',
            field=models.CharField(blank=True, default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='assessment',
            name='university',
            field=smart_selects.db_fields.ChainedForeignKey(auto_choose=True, chained_field='student_country', chained_model_field='country', default=1, on_delete=django.db.models.deletion.CASCADE, to='Master.university'),
            preserve_default=False,
        ),
    ]
