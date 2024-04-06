# Generated by Django 4.2 on 2024-04-06 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Detail_Enquiry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Father_Occupation', models.CharField(blank=True, max_length=100, null=True)),
                ('Father_Annual_Income', models.FloatField(blank=True, null=True)),
                ('Twelveth_Document', models.FileField(blank=True, upload_to='documents/')),
                ('Tenth_Document', models.FileField(blank=True, upload_to='documents/')),
                ('Graduation_Marksheet', models.FileField(blank=True, upload_to='documents/')),
                ('Graduation_Certificate', models.FileField(blank=True, upload_to='documents/')),
                ('UG_Marksheet', models.FileField(blank=True, upload_to='documents/')),
                ('UG_Certificate', models.FileField(blank=True, upload_to='documents/')),
                ('Work_Experience_Document', models.FileField(blank=True, upload_to='documents/')),
                ('Passport_Document', models.FileField(blank=True, upload_to='documents/')),
                ('Offer_Letter', models.FileField(blank=True, upload_to='documents/')),
                ('Ielts_Result', models.FileField(blank=True, upload_to='documents/')),
                ('Toefl_Result', models.FileField(blank=True, upload_to='documents/')),
                ('PTE_Result', models.FileField(blank=True, upload_to='documents/')),
                ('Duolingo_Result', models.FileField(blank=True, upload_to='documents/')),
                ('Gre_Result', models.FileField(blank=True, upload_to='documents/')),
                ('Gmat_Result', models.FileField(blank=True, upload_to='documents/')),
            ],
        ),
    ]
