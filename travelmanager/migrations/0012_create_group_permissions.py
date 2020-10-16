from __future__ import unicode_literals
from itertools import chain

from django.db import migrations


def populate_permissions_lists(apps):
    permission_class = apps.get_model('auth', 'Permission')

    applyvisa_permissions = permission_class.objects.filter(content_type__app_label='travelmanager',
                                                             content_type__model='applyvisa')

    bookflight_permissions = permission_class.objects.filter(content_type__app_label='travelmanager',
                                                          content_type__model='bookflight')

    bookhotel_permissions = permission_class.objects.filter(content_type__app_label='travelmanager',
                                                                  content_type__model='bookhotel')

    flight_permissions = permission_class.objects.filter(content_type__app_label='travelmanager',
                                                                  content_type__model='flight')

    hotel_permissions = permission_class.objects.filter(content_type__app_label='travelmanager',
                                                           content_type__model='hotel')

    manager_permissions = permission_class.objects.filter(content_type__app_label='travelmanager',
                                                         content_type__model='manager')
    registration_permissions = permission_class.objects.filter(content_type__app_label='travelmanager',
                                                          content_type__model='registration')

    traveler_permissions = permission_class.objects.filter(content_type__app_label='travelmanager',
                                                          content_type__model='traveler')

    trip_permissions = permission_class.objects.filter(content_type__app_label='travelmanager',
                                                               content_type__model='trip')
    visa_permissions = permission_class.objects.filter(content_type__app_label='travelmanager',
                                                       content_type__model='visa')


    perm_view_applyvisa = permission_class.objects.filter(content_type__app_label='travelmanager',
                                                           content_type__model='applyvisa',
                                                           codename='view_applyvisa')

    perm_view_bookflight = permission_class.objects.filter(content_type__app_label='travelmanager',
                                                        content_type__model='bookflight',
                                                        codename='view_bookflight')

    perm_view_bookhotel = permission_class.objects.filter(content_type__app_label='travelmanager',
                                                               content_type__model='bookhotel',
                                                               codename='view_bookhotel')

    perm_view_flight = permission_class.objects.filter(content_type__app_label='travelmanager',
                                                               content_type__model='flight',
                                                               codename='view_flight')

    perm_view_hotel = permission_class.objects.filter(content_type__app_label='travelmanager',
                                                         content_type__model='hotel',
                                                         codename='view_hotel')

    perm_view_manager = permission_class.objects.filter(content_type__app_label='travelmanager',
                                                       content_type__model='manager',
                                                       codename='view_manager')
    perm_view_registration = permission_class.objects.filter(content_type__app_label='travelmanager',
                                                        content_type__model='registration',
                                                        codename='view_registration')

    perm_view_traveler = permission_class.objects.filter(content_type__app_label='travelmanager',
                                                        content_type__model='traveler',
                                                        codename='view_traveler')

    perm_view_trip = permission_class.objects.filter(content_type__app_label='travelmanager',
                                                             content_type__model='trip',
                                                             codename='view_trip')

    perm_view_visa= permission_class.objects.filter(content_type__app_label='travelmanager',
                                                     content_type__model='visa',
                                                     codename='view_visa')

    ci_user_permissions = chain(perm_view_applyvisa,
                                perm_view_bookflight,
                                perm_view_bookhotel,
                                perm_view_flight,
                                perm_view_hotel,
                                perm_view_manager,
                                perm_view_registration,
                                perm_view_traveler,
                                perm_view_trip,
                                perm_view_visa)

    ci_scheduler_permissions = chain(applyvisa_permissions,
                                     bookflight_permissions,
                                     bookhotel_permissions,
                                     flight_permissions,
                                     hotel_permissions,
                                     manager_permissions,
                                     trip_permissions,
                                     visa_permissions,

                                     perm_view_traveler,
                                     perm_view_registration)

    ci_registrar_permissions = chain(traveler_permissions,
                                     registration_permissions,
                                     perm_view_applyvisa,
                                     perm_view_bookhotel,
                                     perm_view_bookflight,
                                     perm_view_hotel,
                                     perm_view_flight,
                                     perm_view_manager,
                                     perm_view_trip,
                                     perm_view_visa,
                                     )

    my_groups_initialization_list = [
        {
            "name": "ci_user",
            "permissions_list": ci_user_permissions,
        },
        {
            "name": "ci_scheduler",
            "permissions_list": ci_scheduler_permissions,
        },
        {
            "name": "ci_registrar",
            "permissions_list": ci_registrar_permissions,
        },
    ]
    return my_groups_initialization_list


def add_group_permissions_data(apps, schema_editor):
    groups_initialization_list = populate_permissions_lists(apps)

    Group = apps.get_model('auth', 'Group')
    for group in groups_initialization_list:
        if group['permissions_list'] is not None:
            group_object = Group.objects.get(
                name=group['name']
            )
            group_object.permissions.set(group['permissions_list'])
            group_object.save()


def remove_group_permissions_data(apps, schema_editor):
    groups_initialization_list = populate_permissions_lists(apps)

    Group = apps.get_model('auth', 'Group')
    for group in groups_initialization_list:
        if group['permissions_list'] is not None:
            group_object = Group.objects.get(
                name=group['name']
            )
            list_of_permissions = group['permissions_list']
            for permission in list_of_permissions:
                group_object.permissions.remove(permission)
                group_object.save()


class Migration(migrations.Migration):
    dependencies = [
        ('travelmanager', '0011_create_groups'),
    ]

    operations = [
        migrations.RunPython(
            add_group_permissions_data,
            remove_group_permissions_data
        )
    ]
