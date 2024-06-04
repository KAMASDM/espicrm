# Generated by Django 4.2 on 2024-06-04 06:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Master', '0002_alter_enquiryfollowupstatus_user'),
        ('DetailEnquiry', '0005_alter_detail_enquiry_current_enquiry'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detail_enquiry',
            name='Confirmed_Services',
            field=models.ManyToManyField(blank=True, null=True, to='Master.available_services'),
        ),
        migrations.AlterField(
            model_name='detail_enquiry',
            name='Duolingo_Result',
            field=models.FileField(blank=True, null=True, upload_to='documents/'),
        ),
        migrations.AlterField(
            model_name='detail_enquiry',
            name='Enquiry_Status',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Master.detail_enquiry_status'),
        ),
        migrations.AlterField(
            model_name='detail_enquiry',
            name='Father_Annual_Income',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='detail_enquiry',
            name='Father_Occupation',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='detail_enquiry',
            name='Gmat_Exam',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Master.gmat_exam'),
        ),
        migrations.AlterField(
            model_name='detail_enquiry',
            name='Gmat_Result',
            field=models.FileField(blank=True, null=True, upload_to='documents/'),
        ),
        migrations.AlterField(
            model_name='detail_enquiry',
            name='Graduation_Certificate',
            field=models.FileField(blank=True, null=True, upload_to='documents/'),
        ),
        migrations.AlterField(
            model_name='detail_enquiry',
            name='Graduation_Education_Details',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Graduation_Education_Details', to='Master.edu_level'),
        ),
        migrations.AlterField(
            model_name='detail_enquiry',
            name='Graduation_Marksheet',
            field=models.FileField(blank=True, null=True, upload_to='documents/'),
        ),
        migrations.AlterField(
            model_name='detail_enquiry',
            name='Gre_Exam',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Master.gre_exam'),
        ),
        migrations.AlterField(
            model_name='detail_enquiry',
            name='Gre_Result',
            field=models.FileField(blank=True, null=True, upload_to='documents/'),
        ),
        migrations.AlterField(
            model_name='detail_enquiry',
            name='Ielts_Result',
            field=models.FileField(blank=True, null=True, upload_to='documents/'),
        ),
        migrations.AlterField(
            model_name='detail_enquiry',
            name='Offer_Letter',
            field=models.FileField(blank=True, null=True, upload_to='documents/'),
        ),
        migrations.AlterField(
            model_name='detail_enquiry',
            name='PTE_Exam',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Master.pte_exam'),
        ),
        migrations.AlterField(
            model_name='detail_enquiry',
            name='PTE_Result',
            field=models.FileField(blank=True, null=True, upload_to='documents/'),
        ),
        migrations.AlterField(
            model_name='detail_enquiry',
            name='Passport_Document',
            field=models.FileField(blank=True, null=True, upload_to='documents/'),
        ),
        migrations.AlterField(
            model_name='detail_enquiry',
            name='Refusal',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Master.rejection_reason'),
        ),
        migrations.AlterField(
            model_name='detail_enquiry',
            name='Tenth_Document',
            field=models.FileField(blank=True, null=True, upload_to='documents/'),
        ),
        migrations.AlterField(
            model_name='detail_enquiry',
            name='Tenth_Education_Details',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Tenth_Education_Details', to='Master.edu_level'),
        ),
        migrations.AlterField(
            model_name='detail_enquiry',
            name='Toefl_Exam',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Master.toefl_exam'),
        ),
        migrations.AlterField(
            model_name='detail_enquiry',
            name='Toefl_Result',
            field=models.FileField(blank=True, null=True, upload_to='documents/'),
        ),
        migrations.AlterField(
            model_name='detail_enquiry',
            name='Twelveth_Education_Details',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Twelveth_Education_Details', to='Master.edu_level'),
        ),
        migrations.AlterField(
            model_name='detail_enquiry',
            name='UG_Certificate',
            field=models.FileField(blank=True, null=True, upload_to='documents/'),
        ),
        migrations.AlterField(
            model_name='detail_enquiry',
            name='UG_Marksheet',
            field=models.FileField(blank=True, null=True, upload_to='documents/'),
        ),
        migrations.AlterField(
            model_name='detail_enquiry',
            name='Work_Experience',
            field=models.ForeignKey(blank=True, max_length=100, null=True, on_delete=django.db.models.deletion.CASCADE, to='Master.work_experience'),
        ),
        migrations.AlterField(
            model_name='detail_enquiry',
            name='Work_Experience_Document',
            field=models.FileField(blank=True, null=True, upload_to='documents/'),
        ),
        migrations.AlterField(
            model_name='detail_enquiry',
            name='ielts_Exam',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Master.ielts_exam'),
        ),
    ]