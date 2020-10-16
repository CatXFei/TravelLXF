# Generated by Django 2.2 on 2019-08-10 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travelmanager', '0005_auto_20190810_1502'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='traveler',
            name='passport',
        ),
        migrations.AddField(
            model_name='traveler',
            name='passport_number',
            field=models.CharField(default='', max_length=45),
        ),
        migrations.AddField(
            model_name='traveler',
            name='telephone_nunber',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='manager',
            name='telephone_nunber',
            field=models.TextField(default=''),
        ),
    ]
