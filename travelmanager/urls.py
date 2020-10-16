"""luo_xiaofei_final_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path

from travelmanager.views import (

    TravelerList,
    RegistrationList,
    ManagerList,
    TripList,
    VisaList,
    ApplyVisaList,
    HotelList,
    FlightList,
    BookHotelList,
    BookFlightList,
    ManagerDetail, TravelerDetail, RegistrationDetail, TripDetail, VisaDetail, ApplyVisaDetail, HotelDetail,
    FlightDetail, BookFlightDetail, BookHotelDetail, TravelerCreate, RegistrationCreate, ManagerCreate, TripCreate,
    VisaCreate, ApplyVisaCreate, BookHotelCreate, HotelCreate, FlightCreate, BookFlightCreate, TravelerUpdate,
    RegistrationUpdate, ManagerUpdate, TripUpdate, VisaUpdate, ApplyVisaUpdate, HotelUpdate, BookHotelUpdate,
    FlightUpdate, BookFlightUpdate,
    TripDelete, TravelerDelete, RegistrationDelete, ManagerDelete, VisaDelete, ApplyVisaDelete, BookHotelDelete, HotelDelete, FlightDelete, BookFlightDelete )



urlpatterns = [
    path('traveler/',
         TravelerList.as_view(),
         name='travelmanager_traveler_list_urlpattern'),

    path('traveler/<int:pk>',
         TravelerDetail.as_view(),
         name='travelmanager_traveler_detail_urlpattern'),

    path('traveler/create/',
         TravelerCreate.as_view(),
         name='travelmanager_traveler_create_urlpattern'),

    path('traveler/<int:pk>/update/',
         TravelerUpdate.as_view(),
         name='travelmanager_traveler_update_urlpattern'),

    path('traveler/<int:pk>/delete/',
         TravelerDelete.as_view(),
         name='travelmanager_traveler_delete_urlpattern'),

    path('registration/',
         RegistrationList.as_view(),
         name='travelmanager_registration_list_urlpattern'),

    path('registration/<int:pk>',
         RegistrationDetail.as_view(),
         name='travelmanager_registration_detail_urlpattern'),

    path('registration/create/',
         RegistrationCreate.as_view(),
         name='travelmanager_registration_create_urlpattern'),

    path('registration/<int:pk>/update/',
         RegistrationUpdate.as_view(),
         name='travelmanager_registration_update_urlpattern'),

    path('registration/<int:pk>/delete/',
         RegistrationDelete.as_view(),
         name='travelmanager_registration_delete_urlpattern'),

    path('manager/',
         ManagerList.as_view(),
         name='travelmanager_manager_list_urlpattern'),

    path('manager/<int:pk>',
         ManagerDetail.as_view(),
         name='travelmanager_manager_detail_urlpattern'),

    path('manager/create/',
         ManagerCreate.as_view(),
         name='travelmanager_manager_create_urlpattern'),

    path('manager/<int:pk>/update/',
         ManagerUpdate.as_view(),
         name='travelmanager_manager_update_urlpattern'),

    path('manager/<int:pk>/delete/',
         ManagerDelete.as_view(),
         name='travelmanager_manager_delete_urlpattern'),

    path('trip/',
         TripList.as_view(),
         name='travelmanager_trip_list_urlpattern'),

    path('trip/<int:pk>',
         TripDetail.as_view(),
         name='travelmanager_trip_detail_urlpattern'),

    path('trip/create/',
         TripCreate.as_view(),
         name='travelmanager_trip_create_urlpattern'),

    path('trip/<int:pk>/update/',
         TripUpdate.as_view(),
         name='travelmanager_trip_update_urlpattern'),

    path('trip/<int:pk>/delete/',
         TripDelete.as_view(),
         name='travelmanager_trip_delete_urlpattern'),

    path('visa/',
         VisaList.as_view(),
         name='travelmanager_visa_list_urlpattern'),

    path('visa/<int:pk>',
         VisaDetail.as_view(),
         name='travelmanager_visa_detail_urlpattern'),

    path('visa/create/',
         VisaCreate.as_view(),
         name='travelmanager_visa_create_urlpattern'),

    path('visa/<int:pk>/update/',
         VisaUpdate.as_view(),
         name='travelmanager_visa_update_urlpattern'),

    path('visa/<int:pk>/delete/',
         VisaDelete.as_view(),
         name='travelmanager_visa_delete_urlpattern'),

    path('applyvisa/',
         ApplyVisaList.as_view(),
         name='travelmanager_applyvisa_list_urlpattern'),

    path('applyvisa/<int:pk>',
         ApplyVisaDetail.as_view(),
         name='travelmanager_applyvisa_detail_urlpattern'),

    path('applyvisa/create/',
         ApplyVisaCreate.as_view(),
         name='travelmanager_applyvisa_create_urlpattern'),

    path('applyvisa/<int:pk>/update/',
         ApplyVisaUpdate.as_view(),
         name='travelmanager_applyvisa_update_urlpattern'),

    path('applyvisa/<int:pk>/delete/',
         ApplyVisaDelete.as_view(),
         name='travelmanager_applyvisa_delete_urlpattern'),

    path('hotel/',
         HotelList.as_view(),
         name='travelmanager_hotel_list_urlpattern'),

    path('hotel/<int:pk>',
         HotelDetail.as_view(),
         name='travelmanager_hotel_detail_urlpattern'),

    path('hotel/create/',
         HotelCreate.as_view(),
         name='travelmanager_hotel_create_urlpattern'),

    path('hotel/<int:pk>/update/',
         HotelUpdate.as_view(),
         name='travelmanager_hotel_update_urlpattern'),

    path('hotel/<int:pk>/delete/',
         HotelDelete.as_view(),
         name='travelmanager_hotel_delete_urlpattern'),

    path('bookhotel/',
         BookHotelList.as_view(),
         name='travelmanager_bookhotel_list_urlpattern'),

    path('bookhotel/<int:pk>',
         BookHotelDetail.as_view(),
         name='travelmanager_bookhotel_detail_urlpattern'),

    path('bookhotel/create/',
         BookHotelCreate.as_view(),
         name='travelmanager_bookhotel_create_urlpattern'),

    path('bookhotel/<int:pk>/update/',
         BookHotelUpdate.as_view(),
         name='travelmanager_bookhotel_update_urlpattern'),

    path('bookhotel/<int:pk>/delete/',
         BookHotelDelete.as_view(),
         name='travelmanager_bookhotel_delete_urlpattern'),

    path('flight/',
         FlightList.as_view(),
         name='travelmanager_flight_list_urlpattern'),

    path('flight/<int:pk>',
         FlightDetail.as_view(),
         name='travelmanager_flight_detail_urlpattern'),

    path('flight/create/',
         FlightCreate.as_view(),
         name='travelmanager_flight_create_urlpattern'),

    path('flight/<int:pk>/update/',
         FlightUpdate.as_view(),
         name='travelmanager_flight_update_urlpattern'),

    path('flight/<int:pk>/delete/',
         FlightDelete.as_view(),
         name='travelmanager_flight_delete_urlpattern'),

    path('bookflight/',
         BookFlightList.as_view(),
         name='travelmanager_bookflight_list_urlpattern'),

    path('bookflight/<int:pk>',
         BookFlightDetail.as_view(),
         name='travelmanager_bookflight_detail_urlpattern'),

    path('bookflight/create/',
         BookFlightCreate.as_view(),
         name='travelmanager_bookflight_create_urlpattern'),

    path('bookflight/<int:pk>/update/',
         BookFlightUpdate.as_view(),
         name='travelmanager_bookflight_update_urlpattern'),

    path('bookflight/<int:pk>/delete/',
         BookFlightDelete.as_view(),
         name='travelmanager_bookflight_delete_urlpattern'),

]
