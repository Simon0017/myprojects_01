# Generated by Django 4.2.4 on 2023-09-06 16:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mart', '0003_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='acquisition',
            name='name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='mart.name'),
        ),
    ]