from django.contrib import admin
from .models import Manager, Visa, ApplyVisa, Traveler, Registration, Hotel, BookHotel, Flight, BookFlight, Trip

# Register your models here.


admin.site.register(Manager)
admin.site.register(ApplyVisa)
admin.site.register(Traveler)
admin.site.register(Registration)
admin.site.register(Hotel)
admin.site.register(BookHotel)
admin.site.register(Flight)
admin.site.register(BookFlight)
admin.site.register(Trip)
admin.site.register(Visa)