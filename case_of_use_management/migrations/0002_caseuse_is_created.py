# Generated by Django 3.1.3 on 2023-10-24 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('case_of_use_management', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='caseuse',
            name='is_created',
            field=models.BooleanField(default=True),
        ),
    ]