# Generated by Django 2.2 on 2019-08-10 14:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('travelmanager', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Traveler',
            fields=[
                ('traveler_id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=45)),
                ('last_name', models.CharField(max_length=45)),
                ('passport', models.CharField(max_length=45)),
            ],
            options={
                'ordering': ['last_name', 'first_name'],
                'unique_together': {('last_name', 'first_name')},
            },
        ),
        migrations.RenameModel(
            old_name='BookFlights',
            new_name='BookFlight',
        ),
        migrations.RenameModel(
            old_name='BookHotels',
            new_name='BookHotel',
        ),
        migrations.RenameModel(
            old_name='Flights',
            new_name='Flight',
        ),
        migrations.RenameModel(
            old_name='Hotels',
            new_name='Hotel',
        ),
        migrations.RenameModel(
            old_name='Managers',
            new_name='Manager',
        ),
        migrations.RenameModel(
            old_name='Trips',
            new_name='Trip',
        ),
        migrations.AlterModelOptions(
            name='applyvisa',
            options={'ordering': ['traveler', 'visa']},
        ),
        migrations.AlterModelOptions(
            name='bookflight',
            options={'ordering': ['depart_place', 'destination_place']},
        ),
        migrations.AlterModelOptions(
            name='bookhotel',
            options={'ordering': ['hotel__hotel_place', 'hotel__hotel_name']},
        ),
        migrations.AlterModelOptions(
            name='flight',
            options={'ordering': ['flight_id', 'company']},
        ),
        migrations.AlterModelOptions(
            name='hotel',
            options={'ordering': ['hotel_place', 'hotel_name']},
        ),
        migrations.AlterModelOptions(
            name='manager',
            options={'ordering': ['last_name', 'first_name']},
        ),
        migrations.AlterModelOptions(
            name='registration',
            options={'ordering': ['trip', 'traveler']},
        ),
        migrations.AlterModelOptions(
            name='trip',
            options={'ordering': ['destination_place', 'manager']},
        ),
        migrations.AlterModelOptions(
            name='visa',
            options={'ordering': ['country']},
        ),
        migrations.AlterField(
            model_name='registration',
            name='traveler',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='registration', to='travelmanager.Traveler'),
        ),
        migrations.AlterUniqueTogether(
            name='bookflight',
            unique_together={('depart_place', 'destination_place')},
        ),
        migrations.AlterUniqueTogether(
            name='bookhotel',
            unique_together={('hotel', 'trip')},
        ),
        migrations.AlterUniqueTogether(
            name='flight',
            unique_together={('flight_id', 'company')},
        ),
        migrations.AlterUniqueTogether(
            name='hotel',
            unique_together={('hotel_place', 'hotel_name')},
        ),
        migrations.AlterUniqueTogether(
            name='manager',
            unique_together={('last_name', 'first_name')},
        ),
        migrations.AlterUniqueTogether(
            name='trip',
            unique_together={('destination_place', 'manager')},
        ),
        migrations.DeleteModel(
            name='Travelers',
        ),
        migrations.AddField(
            model_name='applyvisa',
            name='traveler',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, related_name='ApplyVisa', to='travelmanager.Traveler'),
            preserve_default=False,
        ),
        migrations.AlterUniqueTogether(
            name='applyvisa',
            unique_together={('traveler', 'visa')},
        ),
        migrations.AlterUniqueTogether(
            name='registration',
            unique_together={('trip', 'traveler')},
        ),
    ]
