# Generated by Django 4.2.4 on 2023-09-21 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mart', '0010_remove_acquisition_dealer_contact_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='acquisition',
            name='dealer_contact',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='acquisition',
            name='dealer',
            field=models.CharField(max_length=45, null=True),
        ),
    ]
