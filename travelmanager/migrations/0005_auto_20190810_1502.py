# Generated by Django 2.2 on 2019-08-10 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travelmanager', '0004_manager_telephone_nunber'),
    ]

    operations = [
        migrations.AlterField(
            model_name='manager',
            name='telephone_nunber',
            field=models.TimeField(),
        ),
    ]