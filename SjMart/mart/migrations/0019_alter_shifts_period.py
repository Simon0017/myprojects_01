# Generated by Django 4.2.4 on 2023-09-22 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mart', '0018_staff_in_shift'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shifts',
            name='period',
            field=models.CharField(max_length=255),
        ),
    ]
