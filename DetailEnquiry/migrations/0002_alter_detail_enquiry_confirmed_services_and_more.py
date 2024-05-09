# Generated by Django 4.2 on 2024-05-09 04:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Master', '0001_initial'),
        ('DetailEnquiry', '0001_initial'),
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
            name='Graduation_Marksheet',
            field=models.FileField(blank=True, null=True, upload_to='documents/'),
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
            name='Tenth_Document',
            field=models.FileField(blank=True, null=True, upload_to='documents/'),
        ),
        migrations.AlterField(
            model_name='detail_enquiry',
            name='Twelveth_Document',
            field=models.FileField(blank=True, null=True, upload_to='documents/'),
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
            name='Work_Experience_Document',
            field=models.FileField(blank=True, null=True, upload_to='documents/'),
        ),
    ]
