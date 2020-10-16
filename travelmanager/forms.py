from django import forms
from .models import Traveler, Manager, Visa, ApplyVisa, Hotel, Flight, Trip, Registration, BookFlight, BookHotel


class TravelerForm(forms.ModelForm):
    class Meta:
        model = Traveler
        fields = '__all__'

    def clean_first_name(self):
        return self.cleaned_data['first_name'].strip()
    def clean_last_name(self):
        return self.cleaned_data['last_name'].strip()
    def clean_passport_number(self):
        return self.cleaned_data['passport_number'].strip()
    def clean_telephone_nunber(self):
        return self.cleaned_data['telephone_nunber'].strip()


class ManagerForm(forms.ModelForm):
    class Meta:
        model = Manager
        fields = '__all__'

    def clean_first_name(self):
        return self.cleaned_data['first_name'].strip()
    def clean_last_name(self):
        return self.cleaned_data['last_name'].strip()
    def clean_passport_number(self):
        return self.cleaned_data['passport_number'].strip()
    def clean_telephone_nunber(self):
        return self.cleaned_data['telephone_nunber'].strip()


class VisaForm(forms.ModelForm):
    class Meta:
        model = Visa
        fields = '__all__'

    def clean_country(self):
        return self.cleaned_data['country'].strip()


class ApplyVisaForm(forms.ModelForm):
    class Meta:
        model = ApplyVisa
        fields = '__all__'

    def clean_visa_apply_number(self):
        return self.cleaned_data['visa_apply_number'].strip()
    def clean_visa_status(self):
        return self.cleaned_data['visa_status'].strip()


class HotelForm(forms.ModelForm):
    class Meta:
        model = Hotel
        fields = '__all__'

    def clean_hotel_name(self):
        return self.cleaned_data['hotel_name'].strip()

    def clean_hotel_place(self):
        return self.cleaned_data['hotel_place'].strip()


class FlightForm(forms.ModelForm):
    class Meta:
        model = Flight
        fields = '__all__'

    def company(self):
        return self.cleaned_data['company'].strip()


class TripForm(forms.ModelForm):
    class Meta:
        model = Trip
        fields = '__all__'

    def clean_depart_place(self):
        return self.cleaned_data['depart_place'].strip()
    def clean_destination_place(self):
        return self.cleaned_data['destination_place'].strip()



class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = '__all__'

class BookFlightForm(forms.ModelForm):
    class Meta:
        model = BookFlight
        fields = '__all__'

    def clean_depart_place(self):
        return self.cleaned_data['depart_place'].strip()
    def clean_destination_place(self):
        return self.cleaned_data['destination_place'].strip()


class BookHotelForm(forms.ModelForm):
    class Meta:
        model = BookHotel
        fields = '__all__'

    def clean_hotel_upgrade_status(self):
        return self.cleaned_data['hotel_upgrade_status'].strip()
