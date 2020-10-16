from django.db import models
import django.utils.timezone as timezone

# Create your models here.
from django.urls import reverse


class Manager(models.Model):
    manager_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    passport_number = models.CharField(max_length=45, default='')
    telephone_nunber = models.CharField(max_length=45, default='')

    def __str__(self):
        return '%s, %s' % (self.last_name, self.first_name)

    def get_absolute_url(self):
        return reverse('travelmanager_manager_detail_urlpattern',
                       kwargs={'pk':self.pk}
        )

    def get_update_url(self):
        return reverse('travelmanager_manager_update_urlpattern',
                       kwargs={'pk': self.pk}
                       )
    def get_delete_url(self):
        return reverse('travelmanager_manager_delete_urlpattern',
                       kwargs={'pk': self.pk}
                       )
    class Meta:
        ordering = ['last_name', 'first_name']
        unique_together = (('last_name', 'first_name','passport_number'),)


class Visa(models.Model):
    visa_id = models.AutoField(primary_key=True)
    country = models.CharField(max_length=45)

    def __str__(self):
        return '%s' % (self.country)

    def get_absolute_url(self):
        return reverse('travelmanager_visa_detail_urlpattern',
                       kwargs={'pk':self.pk}
        )

    def get_update_url(self):
        return reverse('travelmanager_visa_update_urlpattern',
                       kwargs={'pk': self.pk}
                       )
    def get_delete_url(self):
        return reverse('travelmanager_visa_delete_urlpattern',
                       kwargs={'pk': self.pk}
                       )
    class Meta:
        ordering = ['country']


class Traveler(models.Model):
    traveler_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    passport_number = models.CharField(max_length=45, default='')
    telephone_nunber = models.CharField(max_length=45, default='')

    def __str__(self):
        return '%s, %s' % (self.last_name, self.first_name)

    def get_absolute_url(self):
        return reverse('travelmanager_traveler_detail_urlpattern',
                       kwargs={'pk':self.pk}
        )

    def get_update_url(self):
        return reverse('travelmanager_traveler_update_urlpattern',
                       kwargs={'pk': self.pk}
                       )
    def get_delete_url(self):
        return reverse('travelmanager_traveler_delete_urlpattern',
                       kwargs={'pk': self.pk}
                       )
    class Meta:
        ordering = ['last_name', 'first_name']
        unique_together = (('last_name', 'first_name','passport_number'),)


class ApplyVisa(models.Model):
    apply_visa_id = models.AutoField(primary_key=True)
    visa_apply_number = models.CharField(max_length=45, default='')
    visa_status = models.CharField(max_length=45)
    visa = models.ForeignKey(Visa, related_name= 'ApplyVisa', on_delete=models.PROTECT)
    traveler = models.ForeignKey(Traveler, related_name= 'ApplyVisa', on_delete=models.PROTECT)

    def __str__(self):
        return '%s, %s -- %s' % (self.traveler.last_name, self.traveler.first_name, self.visa.country)

    def get_absolute_url(self):
        return reverse('travelmanager_applyvisa_detail_urlpattern',
                       kwargs={'pk':self.pk}
        )

    def get_update_url(self):
        return reverse('travelmanager_applyvisa_update_urlpattern',
                       kwargs={'pk': self.pk}
                       )
    def get_delete_url(self):
        return reverse('travelmanager_applyvisa_delete_urlpattern',
                       kwargs={'pk': self.pk}
                       )
    class Meta:
        ordering = ['traveler', 'visa']
        unique_together = (('traveler', 'visa'),)



class Hotel(models.Model):
    hotel_id = models.AutoField(primary_key=True)
    hotel_name = models.CharField(max_length=45)
    hotel_place = models.CharField(max_length=45)

    def __str__(self):
        return '%s - %s' % (self.hotel_place, self.hotel_name)

    def get_absolute_url(self):
        return reverse('travelmanager_hotel_detail_urlpattern',
                       kwargs={'pk':self.pk}
        )
    def get_update_url(self):
        return reverse('travelmanager_hotel_update_urlpattern',
                       kwargs={'pk': self.pk}
                       )
    def get_delete_url(self):
        return reverse('travelmanager_hotel_delete_urlpattern',
                       kwargs={'pk': self.pk}
                       )
    class Meta:
        ordering = ['hotel_place', 'hotel_name']
        unique_together = (('hotel_place', 'hotel_name'),)


class Flight(models.Model):
    flight_id = models.AutoField(primary_key=True)
    company = models.CharField(max_length=45)

    def __str__(self):
        return '%s' % (self.company)

    def get_absolute_url(self):
        return reverse('travelmanager_flight_detail_urlpattern',
                       kwargs={'pk':self.pk}
        )
    def get_update_url(self):
        return reverse('travelmanager_flight_update_urlpattern',
                       kwargs={'pk': self.pk}
                       )
    def get_delete_url(self):
        return reverse('travelmanager_flight_delete_urlpattern',
                       kwargs={'pk': self.pk}
                       )
    class Meta:
        ordering = ['flight_id', 'company']
        unique_together = (('flight_id', 'company'),)



class Trip(models.Model):
    trip_id = models.AutoField(primary_key=True)
    depart_place = models.CharField(max_length=45)
    depart_time = models.TimeField(auto_now=False, auto_now_add=False, default=timezone.now)
    destination_place = models.CharField(max_length=45)
    destination_time = models.TimeField(auto_now=False, auto_now_add=False, default=timezone.now)
    total_number = models.IntegerField(default="0")
    ticket_fee = models.IntegerField(default="0")
    dining_fee = models.IntegerField(default="0")
    manager = models.ForeignKey(Manager, related_name='trips', on_delete=models.PROTECT)


    def __str__(self):
        return '%s (%s, %s)' % (self.destination_place, self.manager.last_name, self.manager.first_name)

    def get_absolute_url(self):
        return reverse('travelmanager_trip_detail_urlpattern',
                       kwargs={'pk':self.pk}
        )
    def get_update_url(self):
        return reverse('travelmanager_trip_update_urlpattern',
                       kwargs={'pk': self.pk}
                       )
    def get_delete_url(self):
        return reverse('travelmanager_trip_delete_urlpattern',
                       kwargs={'pk': self.pk}
                       )
    class Meta:
        ordering = ['destination_place', 'manager']
        unique_together = (('destination_place', 'manager'),)


class Registration(models.Model):
    registration_id = models.AutoField(primary_key=True)
    trip = models.ForeignKey(Trip, related_name='registration', on_delete=models.PROTECT)
    traveler = models.ForeignKey(Traveler, related_name='registration', on_delete=models.PROTECT)

    def __str__(self):
        return '%s(%s) - %s, %s' % (self.trip.destination_place, self.trip.manager, self.traveler.last_name, self.traveler.first_name)

    def get_absolute_url(self):
        return reverse('travelmanager_registration_detail_urlpattern',
                       kwargs={'pk':self.pk}
        )
    def get_update_url(self):
        return reverse('travelmanager_registration_update_urlpattern',
                       kwargs={'pk': self.pk}
                       )
    def get_delete_url(self):
        return reverse('travelmanager_registration_delete_urlpattern',
                       kwargs={'pk': self.pk}
                       )
    class Meta:
        ordering = ['trip', 'traveler']
        unique_together = (('trip', 'traveler'),)


class BookFlight(models.Model):
    book_flight_id = models.AutoField(primary_key=True)
    depart_place = models.CharField(max_length=45)
    depart_time = models.TimeField(auto_now=False, auto_now_add=False, default=timezone.now)
    destination_place = models.CharField(max_length=45)
    destination_time = models.TimeField(auto_now=False, auto_now_add=False, default=timezone.now)
    price = models.IntegerField(default="0")
    trip = models.ForeignKey(Trip, related_name='BookFlights', on_delete=models.PROTECT)
    flight = models.ForeignKey(Flight, related_name='BookFlights', on_delete=models.PROTECT)

    def __str__(self):
        return '%s - %s' % (self.depart_place, self.destination_place)

    def get_absolute_url(self):
        return reverse('travelmanager_bookflight_detail_urlpattern',
                       kwargs={'pk':self.pk}
        )
    def get_update_url(self):
        return reverse('travelmanager_bookflight_update_urlpattern',
                       kwargs={'pk': self.pk}
                       )
    def get_delete_url(self):
        return reverse('travelmanager_bookflight_delete_urlpattern',
                       kwargs={'pk': self.pk}
                       )
    class Meta:
        ordering = ['depart_place', 'destination_place']
        unique_together = (('depart_place', 'destination_place'),)


class BookHotel(models.Model):
    book_hotel_id = models.AutoField(primary_key=True)
    hotel_upgrade_status = models.CharField(max_length=45)
    price = models.IntegerField(default="0")
    start_date = models.TimeField(auto_now=False, auto_now_add=False, default=timezone.now)
    end_date = models.TimeField(auto_now=False, auto_now_add=False, default=timezone.now)
    trip = models.ForeignKey(Trip, related_name='BookHotels', on_delete=models.PROTECT)
    hotel = models.ForeignKey(Hotel, related_name='BookHotels', on_delete=models.PROTECT)

    def __str__(self):
        return '%s - %s' % (self.hotel.hotel_place, self.hotel.hotel_name)

    def get_absolute_url(self):
        return reverse('travelmanager_bookhotel_detail_urlpattern',
                       kwargs={'pk':self.pk}
        )
    def get_update_url(self):
        return reverse('travelmanager_bookhotel_update_urlpattern',
                       kwargs={'pk': self.pk}
                       )
    def get_delete_url(self):
        return reverse('travelmanager_bookhotel_delete_urlpattern',
                       kwargs={'pk': self.pk}
                       )
    class Meta:
        ordering = ['hotel__hotel_place', 'hotel__hotel_name']
        unique_together = (('hotel', 'trip'),)
