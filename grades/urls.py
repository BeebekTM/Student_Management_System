from django.urls import path
from . import views

urlpatterns = [

    path(
        'grades/',
        views.grade_list,
        name='grade_list'
    ),

    path(
        'grades/add/',
        views.grade_create,
        name='grade_create'
    ),
]