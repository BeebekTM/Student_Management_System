from django.urls import path
from . import views

urlpatterns = [

    path(
        'attendance/',
        views.attendance_list,
        name='attendance_list'
    ),

    path(
        'attendance/add/',
        views.attendance_create,
        name='attendance_create'
    ),
]