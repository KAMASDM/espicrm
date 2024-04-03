# Generated by Django 4.2 on 2024-04-02 07:05

from django.db import migrations, models
import django.db.models.deletion
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('Enquiry', '0011_alter_enquiry_source_enquiry'),
    ]

    operations = [
        migrations.CreateModel(
            name='Continent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('continent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Enquiry.continent')),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=50)),
                ('street', models.CharField(max_length=100)),
                ('continent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Enquiry.continent')),
                ('country', smart_selects.db_fields.ChainedForeignKey(auto_choose=True, chained_field='continent', chained_model_field='continent', on_delete=django.db.models.deletion.CASCADE, to='Enquiry.country')),
            ],
        ),
    ]