from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, get_object_or_404, render_to_response, redirect
from django.http.response import HttpResponse
from django.template import loader
from django.views import View
from django.views.generic import ListView, CreateView, UpdateView

from travelmanager.forms import TripForm, RegistrationForm, ManagerForm, TravelerForm, VisaForm, ApplyVisaForm, \
    HotelForm, BookHotelForm, FlightForm, BookFlightForm
from travelmanager.utils import PageLinksMixin
from .models import (
     Trip,
     Registration,
     Manager,
     Traveler,
     Visa,
     ApplyVisa,
     Hotel,
     Flight,
     BookFlight,
     BookHotel,
)

class TripList(LoginRequiredMixin,PermissionRequiredMixin,ListView):
    model = Trip
    permission_required = 'travelmanager.view_trip'

# class TripList(View):
#     def get(self, request):
#         return render(
#             request,
#             'travelmanager/trip_list.html',
#             {'trip_list': Trip.objects.all()}
#         )

class TripDetail(LoginRequiredMixin,PermissionRequiredMixin,View):
    permission_required = 'travelmanager.view_trip'

    def get(self, request, pk):
        trip = get_object_or_404(
            Trip,
            pk = pk
        )

        registration_list = trip.registration.all()
        bookhotel_list = trip.BookHotels.all()
        bookflight_list = trip.BookFlights.all()

        return render_to_response(
            'travelmanager/trip_detail.html',
            {'trip': trip, 'registration_list': registration_list, 'bookhotel_list': bookhotel_list, 'bookflight_list': bookflight_list}
        )

class TripCreate(LoginRequiredMixin,PermissionRequiredMixin,CreateView):
    permission_required = 'travelmanager.add_trip'

    form_class = TripForm
    model = Trip

# class TripCreate(ObjectCreateMixin, View):
#     form_class = TripForm
#     template_name = 'travelmanager/trip_form.html'

class TripUpdate(LoginRequiredMixin,PermissionRequiredMixin,UpdateView):
    permission_required = 'travelmanager.change_trip'

    form_class = TripForm
    model = Trip
    template_name = 'travelmanager/trip_form_update.html'

# class TripUpdate(View):
#     form_class = TripForm
#     model = Trip
#     template_name = 'travelmanager/trip_form_update.html'
#
#     def get_object(self, pk):
#         return get_object_or_404(
#             self.model,
#             pk=pk,
#         )
#
#     def get(self, request, pk):
#         trip = self.get_object(pk)
#         context={
#             'form': self.form_class(
#                 instance=trip),
#             'trip': trip,
#         }
#         return render(
#             request, self.template_name, context
#         )
#
#     def post(self, request, pk):
#         trip = self.get_object(pk)
#         bound_form = self.form_class(
#             request.POST, instance=trip)
#         if bound_form.is_valid():
#             new_trip = bound_form.save()
#             return redirect(new_trip)
#         else:
#             context = {
#                 'form': bound_form,
#                 'trip': trip,
#             }
#             return render(
#                 request,
#                 self.template_name,
#                 context
#             )


class TripDelete(LoginRequiredMixin,PermissionRequiredMixin,View):
    permission_required = 'travelmanager.delete_trip'

    def get(self, request, pk):
        trip = self.get_object(pk)
        registrations = trip.registration.all()

        if registrations.count() > 0:
            return render(
                request,
                'travelmanager/trip_refuse_delete.html',
                {
                    'trip': trip,
                    'registrations': registrations
                }
            )
        else:
            return render(
                request,
                'travelmanager/trip_confirm_delete.html',
                {'trip': trip}
            )
    def get_object(self, pk):
        return get_object_or_404(
            Trip,
            pk=pk
        )
    def post(self, request, pk):
        trip = self.get_object(pk)
        trip.delete()
        return redirect('travelmanager_trip_list_urlpattern')

class RegistrationList(LoginRequiredMixin,PermissionRequiredMixin,ListView):
    permission_required = 'travelmanager.view_registration'
    model = Registration

# class RegistrationList(View):
#     def get(self, request):
#         return render(
#             request,
#             'travelmanager/registration_list.html',
#             {'registration_list': Registration.objects.all()}
#         )

class RegistrationDetail(LoginRequiredMixin,PermissionRequiredMixin,View):
    permission_required = 'travelmanager.view_registration'

    def get(self, request, pk):
        registration = get_object_or_404(
            Registration,
            pk = pk
        )

        return render_to_response(
            'travelmanager/registration_detail.html',
            {'registration': registration}
        )


class RegistrationCreate(LoginRequiredMixin,PermissionRequiredMixin,CreateView):
    permission_required = 'travelmanager.add_registration'

    form_class = RegistrationForm
    model = Registration


# class RegistrationCreate(ObjectCreateMixin, View):
#     form_class = RegistrationForm
#     template_name = 'travelmanager/registration_form.html'

class RegistrationUpdate(LoginRequiredMixin,PermissionRequiredMixin,UpdateView):
    permission_required = 'travelmanager.change_registration'

    form_class = RegistrationForm
    model = Registration
    template_name = 'travelmanager/registration_form_update.html'

# class RegistrationUpdate(View):
#     form_class = RegistrationForm
#     model = Registration
#     template_name = 'travelmanager/registration_form_update.html'
#
#     def get_object(self, pk):
#         return get_object_or_404(
#             self.model,
#             pk=pk,
#         )
#
#     def get(self, request, pk):
#         registration = self.get_object(pk)
#         context={
#             'form': self.form_class(
#                 instance=registration),
#             'registration': registration,
#         }
#         return render(
#             request, self.template_name, context
#         )
#
#     def post(self, request, pk):
#         registration = self.get_object(pk)
#         bound_form = self.form_class(
#             request.POST, instance=registration)
#         if bound_form.is_valid():
#             new_registration = bound_form.save()
#             return redirect(new_registration)
#         else:
#             context = {
#                 'form': bound_form,
#                 'registration': registration,
#             }
#             return render(
#                 request,
#                 self.template_name,
#                 context
#             )


class RegistrationDelete(LoginRequiredMixin,PermissionRequiredMixin,View):
    permission_required = 'travelmanager.delete_registration'

    def get(self, request, pk):
        registration = self.get_object(pk)

        return render(
                request,
                'travelmanager/registration_confirm_delete.html',
                {'registration': registration}
        )
    def get_object(self, pk):
        return get_object_or_404(
            Registration,
            pk=pk
        )
    def post(self, request, pk):
        registration = self.get_object(pk)
        registration.delete()
        return redirect('travelmanager_registration_list_urlpattern')

class ManagerList(LoginRequiredMixin,PermissionRequiredMixin,ListView):
    permission_required = 'travelmanager.view_manager'

    model = Manager


# class ManagerList(View):
#     def get(self, request):
#         return render(
#             request,
#             'travelmanager/manager_list.html',
#             {'manager_list': Manager.objects.all()}
#         )

class ManagerDetail(LoginRequiredMixin,PermissionRequiredMixin,View):
    permission_required = 'travelmanager.view_manager'

    def get(self, request, pk):
        manager = get_object_or_404(
            Manager,
            pk = pk
        )

        trip_list = manager.trips.all()

        return render_to_response(
            'travelmanager/manager_detail.html',
            {'manager':manager, 'trip_list': trip_list}
        )
class ManagerCreate(LoginRequiredMixin,PermissionRequiredMixin,CreateView):
    permission_required = 'travelmanager.add_manager'

    form_class = ManagerForm
    model = Manager

# class ManagerCreate(ObjectCreateMixin, View):
#     form_class = ManagerForm
#     template_name = 'travelmanager/manager_form.html'

class ManagerUpdate(LoginRequiredMixin,PermissionRequiredMixin,UpdateView):
    permission_required = 'travelmanager.change_manager'

    form_class = ManagerForm
    model = Manager
    template_name = 'travelmanager/manager_form_update.html'

# class ManagerUpdate(View):
#     form_class = ManagerForm
#     model = Manager
#     template_name = 'travelmanager/manager_form_update.html'
#
#     def get_object(self, pk):
#         return get_object_or_404(
#             self.model,
#             pk=pk,
#         )
#
#     def get(self, request, pk):
#         manager = self.get_object(pk)
#         context={
#             'form': self.form_class(
#                 instance=manager),
#             'manager': manager,
#         }
#         return render(
#             request, self.template_name, context
#         )
#
#     def post(self, request, pk):
#         manager = self.get_object(pk)
#         bound_form = self.form_class(
#             request.POST, instance=manager)
#         if bound_form.is_valid():
#             new_manager = bound_form.save()
#             return redirect(new_manager)
#         else:
#             context = {
#                 'form': bound_form,
#                 'manager': manager,
#             }
#             return render(
#                 request,
#                 self.template_name,
#                 context
#             )


class ManagerDelete(LoginRequiredMixin,PermissionRequiredMixin,View):
    permission_required = 'travelmanager.delete_manager'

    def get(self, request, pk):
        manager = self.get_object(pk)
        trips = manager.trips.all()
        if trips.count() > 0:
            return render(
                request,
                'travelmanager/manager_refuse_delete.html',
                {
                    'manager': manager,
                    'trips': trips
                }
            )
        else:
            return render(
                request,
                'travelmanager/manager_confirm_delete.html',
                {'manager': manager}
            )

    def get_object(self, pk):
        return get_object_or_404(
            Manager,
            pk=pk
        )

    def post(self, request, pk):
        manager = self.get_object(pk)
        manager.delete()
        return redirect('travelmanager_manager_list_urlpattern')



class TravelerList(LoginRequiredMixin,PermissionRequiredMixin,PageLinksMixin, ListView):
    permission_required = 'travelmanager.view_traveler'

    paginate_by = 25
    model = Traveler

# class TravelerList(View):
#     page_kwarg = 'page'
#     paginate_by = 25;
#     template_name = 'travelmanager/traveler_list.html'
#
#     def get(self, request):
#         travelers = Traveler.objects.all()
#         paginator = Paginator(
#             travelers,
#             self.paginate_by
#         )
#         page_number = request.GET.get(
#             self.page_kwarg
#         )
#         try:
#             page = paginator.page(page_number)
#         except PageNotAnInteger:
#             page = paginator.page(1)
#         except EmptyPage:
#             page = paginator.page(
#                 paginator.num_pages
#             )
#         if page.has_previous():
#             prev_url = "?{pkw}={n}".format(
#                 pkw=self.page_kwarg,
#                 n=page.previous_page_number())
#
#         else:
#             prev_url = None
#         if page.has_next():
#             next_url = "?{pkw}={n}".format(
#                 pkw=self.page_kwarg,
#                 n=page.next_page_number())
#
#         else:
#             next_url = None
#
#         context = {
#             'is_paginated':
#                 page.has_other_pages(),
#             'next_page_url': next_url,
#             'paginator': paginator,
#             'previous_page_url': prev_url,
#             'traveler_list': page,
#         }
#         return render(
#             request, self.template_name, context
#         )
#
class TravelerDetail(LoginRequiredMixin,PermissionRequiredMixin,View):
    permission_required = 'travelmanager.view_traveler'

    def get(self, request, pk):
        traveler = get_object_or_404(
            Traveler,
            pk = pk
        )

        registration_list = traveler.registration.all()
        applyvisa_list = traveler.ApplyVisa.all()

        return render_to_response(
            'travelmanager/traveler_detail.html',
            {'traveler': traveler, 'registration_list': registration_list, 'applyvisa_list': applyvisa_list}
        )

class TravelerCreate(LoginRequiredMixin,PermissionRequiredMixin,CreateView):
    permission_required = 'travelmanager.add_travelers'

    form_class = TravelerForm
    model = Traveler

# class TravelerCreate(ObjectCreateMixin, View):
#     form_class = TravelerForm
#     template_name = 'travelmanager/traveler_form.html'

class TravelerUpdate(LoginRequiredMixin,PermissionRequiredMixin,UpdateView):
    permission_required = 'travelmanager.change_travelers'

    form_class = TravelerForm
    model = Traveler
    template_name = 'travelmanager/traveler_form_update.html'

# class TravelerUpdate(View):
#     form_class = TravelerForm
#     model = Traveler
#     template_name = 'travelmanager/traveler_form_update.html'
#
#     def get_object(self, pk):
#         return get_object_or_404(
#             self.model,
#             pk=pk,
#         )
#
#     def get(self, request, pk):
#         traveler = self.get_object(pk)
#         context={
#             'form': self.form_class(
#                 instance=traveler),
#             'traveler': traveler,
#         }
#         return render(
#             request, self.template_name, context
#         )
#
#     def post(self, request, pk):
#         traveler = self.get_object(pk)
#         bound_form = self.form_class(
#             request.POST, instance=traveler)
#         if bound_form.is_valid():
#             new_traveler = bound_form.save()
#             return redirect(new_traveler)
#         else:
#             context = {
#                 'form': bound_form,
#                 'traveler': traveler,
#             }
#             return render(
#                 request,
#                 self.template_name,
#                 context
#             )

class TravelerDelete(LoginRequiredMixin,PermissionRequiredMixin,View):
    permission_required = 'travelmanager.delete_travelers'

    def get(self, request, pk):
        traveler = self.get_object(pk)
        registrations = traveler.registration.all()
        if registrations.count() > 0:
            return render(
                request,
                'travelmanager/traveler_refuse_delete.html',
                {
                    'traveler': traveler,
                    'registrations': registrations
                }
            )
        else:
            return render(
                request,
                'travelmanager/traveler_confirm_delete.html',
                {'traveler': traveler}
            )

    def get_object(self, pk):
        return get_object_or_404(
            Traveler,
            pk=pk
        )

    def post(self, request, pk):
        traveler = self.get_object(pk)
        traveler.delete()
        return redirect('travelmanager_traveler_list_urlpattern')

class VisaList(LoginRequiredMixin,PermissionRequiredMixin,ListView):
    permission_required = 'travelmanager.view_visa'

    model = Visa

# class VisaList(View):
#     def get(self, request):
#         return render(
#             request,
#             'travelmanager/visa_list.html',
#             {'visa_list': Visa.objects.all()}
#         )

class VisaDetail(LoginRequiredMixin,PermissionRequiredMixin,View):
    permission_required = 'travelmanager.view_visa'

    def get(self, request, pk):
        visa = get_object_or_404(
            Visa,
            pk = pk
        )

        applyvisa_list = visa.ApplyVisa.all()

        return render_to_response(
            'travelmanager/visa_detail.html',
            {'visa':visa, 'applyvisa_list': applyvisa_list}
        )

class VisaCreate(LoginRequiredMixin,PermissionRequiredMixin,CreateView):
    permission_required = 'travelmanager.add_visa'

    form_class = VisaForm
    model = Visa

# class VisaCreate(ObjectCreateMixin, View):
#     form_class = VisaForm
#     template_name = 'travelmanager/visa_form.html'

class VisaUpdate(LoginRequiredMixin,PermissionRequiredMixin,UpdateView):
    permission_required = 'travelmanager.change_visa'

    form_class = VisaForm
    model = Visa
    template_name = 'travelmanager/visa_form_update.html'

# class VisaUpdate(View):
#     form_class = VisaForm
#     model = Visa
#     template_name = 'travelmanager/visa_form_update.html'
#
#     def get_object(self, pk):
#         return get_object_or_404(
#             self.model,
#             pk=pk,
#         )
#
#     def get(self, request, pk):
#         visa = self.get_object(pk)
#         context={
#             'form': self.form_class(
#                 instance=visa),
#             'visa': visa,
#         }
#         return render(
#             request, self.template_name, context
#         )
#
#     def post(self, request, pk):
#         visa = self.get_object(pk)
#         bound_form = self.form_class(
#             request.POST, instance=visa)
#         if bound_form.is_valid():
#             new_visa= bound_form.save()
#             return redirect(new_visa)
#         else:
#             context = {
#                 'form': bound_form,
#                 'visa': visa,
#             }
#             return render(
#                 request,
#                 self.template_name,
#                 context
#             )

class VisaDelete(LoginRequiredMixin,PermissionRequiredMixin,View):
    permission_required = 'travelmanager.delete_visa'

    def get(self, request, pk):
        visa = self.get_object(pk)
        applyvisas = visa.ApplyVisa.all()
        if applyvisas.count() > 0:
            return render(
                request,
                'travelmanager/visa_refuse_delete.html',
                {
                    'visa': visa,
                    'applyvisas': applyvisas
                }
            )
        else:
            return render(
                request,
                'travelmanager/visa_confirm_delete.html',
                {'visa': visa}
            )

    def get_object(self, pk):
        return get_object_or_404(
            Visa,
            pk=pk
        )

    def post(self, request, pk):
        visa = self.get_object(pk)
        visa.delete()
        return redirect('travelmanager_visa_list_urlpattern')

class ApplyVisaList(LoginRequiredMixin,PermissionRequiredMixin,View):
    permission_required = 'travelmanager.view_applyvisa'

    def get(self, request):
        return render(
            request,
            'travelmanager/applyvisa_list.html',
            {'applyvisa_list': ApplyVisa.objects.all()}
        )

class ApplyVisaDetail(LoginRequiredMixin,PermissionRequiredMixin,View):
    permission_required = 'travelmanager.view_applyvisa'

    def get(self, request, pk):
        applyvisa = get_object_or_404(
            ApplyVisa,
            pk = pk
        )

        return render_to_response(
            'travelmanager/applyvisa_detail.html',
            {'applyvisa':applyvisa}
        )

class ApplyVisaCreate(LoginRequiredMixin,PermissionRequiredMixin,CreateView):
    permission_required = 'travelmanager.add_applyvisa'

    form_class = ApplyVisaForm
    model = ApplyVisa

# class ApplyVisaCreate(ObjectCreateMixin, View):
#     form_class = ApplyVisaForm
#     template_name = 'travelmanager/applyvisa_form.html'

class ApplyVisaUpdate(LoginRequiredMixin,PermissionRequiredMixin,UpdateView):
    permission_required = 'travelmanager.change_applyvisa'

    form_class = ApplyVisaForm
    model = ApplyVisa
    template_name = 'travelmanager/applyvisa_form_update.html'

# class ApplyVisaUpdate(View):
#     form_class = ApplyVisaForm
#     model = ApplyVisa
#     template_name = 'travelmanager/applyvisa_form_update.html'
#
#     def get_object(self, pk):
#         return get_object_or_404(
#             self.model,
#             pk=pk,
#         )
#
#     def get(self, request, pk):
#         applyvisa = self.get_object(pk)
#         context={
#             'form': self.form_class(
#                 instance=applyvisa),
#             'applyvisa': applyvisa,
#         }
#         return render(
#             request, self.template_name, context
#         )
#
#     def post(self, request, pk):
#         applyvisa = self.get_object(pk)
#         bound_form = self.form_class(
#             request.POST, instance=applyvisa)
#         if bound_form.is_valid():
#             new_applyvisa= bound_form.save()
#             return redirect(new_applyvisa)
#         else:
#             context = {
#                 'form': bound_form,
#                 'applyvisa': applyvisa,
#             }
#             return render(
#                 request,
#                 self.template_name,
#                 context
#             )

class ApplyVisaDelete(LoginRequiredMixin,PermissionRequiredMixin,View):
    permission_required = 'travelmanager.delete_applyvisa'

    def get(self, request, pk):
        applyvisa = self.get_object(pk)

        return render(
                request,
                'travelmanager/applyvisa_confirm_delete.html',
                {'applyvisa': applyvisa}
        )
    def get_object(self, pk):
        return get_object_or_404(
            ApplyVisa,
            pk=pk
        )
    def post(self, request, pk):
        applyvisa = self.get_object(pk)
        applyvisa.delete()
        return redirect('travelmanager_applyvisa_list_urlpattern')

class HotelList(LoginRequiredMixin,PermissionRequiredMixin,ListView):
    permission_required = 'travelmanager.view_hotel'

    model = Hotel

# class HotelList(View):
#     def get(self, request):
#         return render(
#             request,
#             'travelmanager/hotel_list.html',
#             {'hotel_list': Hotel.objects.all()}
#         )

class HotelDetail(LoginRequiredMixin,PermissionRequiredMixin,View):
    permission_required = 'travelmanager.view_hotel'

    def get(self, request, pk):
        hotel = get_object_or_404(
            Hotel,
            pk = pk
        )
        bookhotel_list = hotel.BookHotels.all()
        return render_to_response(
            'travelmanager/hotel_detail.html',
            {'hotel':hotel,'bookhotel_list':bookhotel_list
             }
        )

class HotelCreate(LoginRequiredMixin,PermissionRequiredMixin,CreateView):
    permission_required = 'travelmanager.add_hotel'

    form_class = HotelForm
    model = Hotel

# class HotelCreate(ObjectCreateMixin, View):
#     form_class = HotelForm
#     template_name = 'travelmanager/hotel_form.html'

class HotelUpdate(LoginRequiredMixin,PermissionRequiredMixin,UpdateView):
    permission_required = 'travelmanager.change_hotel'

    form_class = HotelForm
    model = Hotel
    template_name = 'travelmanager/hotel_form_update.html'

# class HotelUpdate(View):
#     form_class = HotelForm
#     model = Hotel
#     template_name = 'travelmanager/hotel_form_update.html'
#
#     def get_object(self, pk):
#         return get_object_or_404(
#             self.model,
#             pk=pk,
#         )
#
#     def get(self, request, pk):
#         hotel = self.get_object(pk)
#         context={
#             'form': self.form_class(
#                 instance=hotel),
#             'hotel': hotel,
#         }
#         return render(
#             request, self.template_name, context
#         )
#
#     def post(self, request, pk):
#         hotel= self.get_object(pk)
#         bound_form = self.form_class(
#             request.POST, instance=hotel)
#         if bound_form.is_valid():
#             new_hotel= bound_form.save()
#             return redirect(new_hotel)
#         else:
#             context = {
#                 'form': bound_form,
#                 'hotel': hotel,
#             }
#             return render(
#                 request,
#                 self.template_name,
#                 context
#             )
class HotelDelete(LoginRequiredMixin,PermissionRequiredMixin,View):
    permission_required = 'travelmanager.delete_hotel'

    def get(self, request, pk):
        hotel = self.get_object(pk)
        bookhotels = hotel.BookHotels.all()

        if bookhotels.count() > 0:
            return render(
                request,
                'travelmanager/hotel_refuse_delete.html',
                {
                    'hotel': hotel,
                    'bookhotels': bookhotels
                }
            )
        else:
            return render(
                request,
                'travelmanager/hotel_confirm_delete.html',
                {'hotel': hotel}
            )

    def get_object(self, pk):
        return get_object_or_404(
            Hotel,
            pk=pk
        )

    def post(self, request, pk):
        hotel = self.get_object(pk)
        hotel.delete()
        return redirect('travelmanager_hotel_list_urlpattern')


class BookHotelList(LoginRequiredMixin,PermissionRequiredMixin,View):
    permission_required = 'travelmanager.view_bookhotel'

    def get(self, request):
        return render(
            request,
            'travelmanager/bookhotel_list.html',
            {'bookhotel_list': BookHotel.objects.all()}
        )

class BookHotelDetail(LoginRequiredMixin,PermissionRequiredMixin,View):
    permission_required = 'travelmanager.view_bookhotel'

    def get(self, request, pk):
        bookhotel = get_object_or_404(
            BookHotel,
            pk = pk
        )

        return render_to_response(
            'travelmanager/bookhotel_detail.html',
            {'bookhotel': bookhotel}
        )
class BookHotelCreate(LoginRequiredMixin,PermissionRequiredMixin,CreateView):
    permission_required = 'travelmanager.add_bookhotel'

    form_class = BookHotelForm
    model = BookHotel

# class BookHotelCreate(ObjectCreateMixin, View):
#     form_class = BookHotelForm
#     template_name = 'travelmanager/bookhotel_form.html'


class BookHotelUpdate(LoginRequiredMixin,PermissionRequiredMixin,UpdateView):
    permission_required = 'travelmanager.change_bookhotel'

    form_class = BookHotelForm
    model = BookHotel
    template_name = 'travelmanager/bookhotel_form_update.html'

# class BookHotelUpdate(View):
#     form_class = BookHotelForm
#     model = BookHotel
#     template_name = 'travelmanager/bookhotel_form_update.html'
#
#     def get_object(self, pk):
#         return get_object_or_404(
#             self.model,
#             pk=pk,
#         )
#
#     def get(self, request, pk):
#         bookhotel = self.get_object(pk)
#         context={
#             'form': self.form_class(
#                 instance=bookhotel),
#             'bookhotel': bookhotel,
#         }
#         return render(
#             request, self.template_name, context
#         )
#
#     def post(self, request, pk):
#         bookhotel= self.get_object(pk)
#         bound_form = self.form_class(
#             request.POST, instance=bookhotel)
#         if bound_form.is_valid():
#             new_bookhotel= bound_form.save()
#             return redirect(new_bookhotel)
#         else:
#             context = {
#                 'form': bound_form,
#                 'bookhotel': bookhotel,
#             }
#             return render(
#                 request,
#                 self.template_name,
#                 context
#             )

class BookHotelDelete(LoginRequiredMixin,PermissionRequiredMixin,View):
    permission_required = 'travelmanager.delete_bookflight'

    def get(self, request, pk):
        bookhotel = self.get_object(pk)

        return render(
                request,
                'travelmanager/bookhotel_confirm_delete.html',
                {'bookhotel': bookhotel}
        )
    def get_object(self, pk):
        return get_object_or_404(
            BookHotel,
            pk=pk
        )
    def post(self, request, pk):
        bookhotel = self.get_object(pk)
        bookhotel.delete()
        return redirect('travelmanager_bookhotel_list_urlpattern')

class FlightList(LoginRequiredMixin,PermissionRequiredMixin,ListView):
    permission_required = 'travelmanager.view_flight'

    model = Flight

# class FlightList(View):
#     def get(self, request):
#         return render(
#             request,
#             'travelmanager/flight_list.html',
#             {'flight_list': Flight.objects.all()}
#         )

class FlightDetail(LoginRequiredMixin,PermissionRequiredMixin,View):

    permission_required = 'travelmanager.view_flight'
    def get(self, request, pk):
        flight = get_object_or_404(
            Flight,
            pk = pk
        )
        bookflight_list = flight.BookFlights.all()
        return render_to_response(
            'travelmanager/flight_detail.html',
            {'flight':flight,'bookflight_list':bookflight_list}
        )

class FlightCreate(LoginRequiredMixin,PermissionRequiredMixin,CreateView):
    permission_required = 'travelmanager.add_flight'

    form_class = FlightForm
    model = Flight

# class FlightCreate(ObjectCreateMixin, View):
#     form_class = FlightForm
#     template_name = 'travelmanager/flight_form.html'

class FlightUpdate(LoginRequiredMixin,PermissionRequiredMixin,UpdateView):
    permission_required = 'travelmanager.change_flight'

    form_class = FlightForm
    model = Flight
    template_name = 'travelmanager/flight_form_update.html'

# class FlightUpdate(View):
#     form_class = FlightForm
#     model = Flight
#     template_name = 'travelmanager/flight_form_update.html'
#
#     def get_object(self, pk):
#         return get_object_or_404(
#             self.model,
#             pk=pk,
#         )
#
#     def get(self, request, pk):
#         flight = self.get_object(pk)
#         context={
#             'form': self.form_class(
#                 instance=flight),
#             'flight': flight,
#         }
#         return render(
#             request, self.template_name, context
#         )
#
#     def post(self, request, pk):
#         flight= self.get_object(pk)
#         bound_form = self.form_class(
#             request.POST, instance=flight)
#         if bound_form.is_valid():
#             new_flight= bound_form.save()
#             return redirect(new_flight)
#         else:
#             context = {
#                 'form': bound_form,
#                 'flight': flight,
#             }
#             return render(
#                 request,
#                 self.template_name,
#                 context
#             )


class FlightDelete(LoginRequiredMixin,PermissionRequiredMixin,View):
    permission_required = 'travelmanager.delete_flight'

    def get(self, request, pk):
        flight = self.get_object(pk)
        bookflights = flight.BookFlights.all()

        if bookflights.count() > 0:
            return render(
                request,
                'travelmanager/flight_refuse_delete.html',
                {
                    'flight': flight,
                    'bookflights': bookflights
                }
            )
        else:
            return render(
                request,
                'travelmanager/flight_confirm_delete.html',
                {'flight': flight}
            )

    def get_object(self, pk):
        return get_object_or_404(
            Flight,
            pk=pk
        )

    def post(self, request, pk):
        flight = self.get_object(pk)
        flight.delete()
        return redirect('travelmanager_flight_list_urlpattern')

class BookFlightList(LoginRequiredMixin,PermissionRequiredMixin,View):
    permission_required = 'travelmanager.view_bookflight'

    def get(self, request):
        return render(
            request,
            'travelmanager/bookflight_list.html',
            {'bookflight_list': BookFlight.objects.all()}
        )

class BookFlightDetail(LoginRequiredMixin,PermissionRequiredMixin,View):
    permission_required = 'travelmanager.view_bookflight'

    def get(self, request, pk):
        bookflight = get_object_or_404(
            BookFlight,
            pk = pk
        )

        return render_to_response(
            'travelmanager/bookflight_detail.html',
            {'bookflight': bookflight}
        )
class BookFlightCreate(LoginRequiredMixin,PermissionRequiredMixin,CreateView):
    permission_required = 'travelmanager.add_bookflight'
    form_class = BookFlightForm
    model = BookFlight

# class BookFlightCreate(ObjectCreateMixin, View):
#     form_class = BookFlightForm
#     template_name = 'travelmanager/bookflight_form.html'

class BookFlightUpdate(LoginRequiredMixin,PermissionRequiredMixin,UpdateView):
    permission_required = 'travelmanager.change_bookflight'

    form_class = BookFlightForm
    model = BookFlight
    template_name = 'travelmanager/bookflight_form_update.html'

# class BookFlightUpdate(View):
#     form_class = BookFlightForm
#     model = BookFlight
#     template_name = 'travelmanager/bookflight_form_update.html'
#
#     def get_object(self, pk):
#         return get_object_or_404(
#             self.model,
#             pk=pk,
#         )
#
#     def get(self, request, pk):
#         bookflight = self.get_object(pk)
#         context={
#             'form': self.form_class(
#                 instance=bookflight),
#             'bookflight': bookflight,
#         }
#         return render(
#             request, self.template_name, context
#         )
#
#     def post(self, request, pk):
#         bookflight= self.get_object(pk)
#         bound_form = self.form_class(
#             request.POST, instance=bookflight)
#         if bound_form.is_valid():
#             new_bookflight= bound_form.save()
#             return redirect(new_bookflight)
#         else:
#             context = {
#                 'form': bound_form,
#                 'bookflight': bookflight,
#             }
#             return render(
#                 request,
#                 self.template_name,
#                 context
#             )

class BookFlightDelete(LoginRequiredMixin,PermissionRequiredMixin,View):
    permission_required = 'travelmanager.delete_bookflight'

    def get(self, request, pk):
        bookflight = self.get_object(pk)

        return render(
                request,
                'travelmanager/bookflight_confirm_delete.html',
                {'bookflight': bookflight}
        )
    def get_object(self, pk):
        return get_object_or_404(
            BookFlight,
            pk=pk
        )
    def post(self, request, pk):
        bookflight = self.get_object(pk)
        bookflight.delete()
        return redirect('travelmanager_bookflight_list_urlpattern')
