# Generated by Django 3.1.3 on 2023-11-02 00:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('incident_handler_management', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='incident',
            name='number_of_use_cases',
            field=models.PositiveIntegerField(default=0),
        ),
    ]