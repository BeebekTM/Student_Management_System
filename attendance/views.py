from django.shortcuts import render, redirect
from .forms import AttendanceForm
from .models import Attendance



def attendance_create(request):

    if request.method == "POST":

        form = AttendanceForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("attendance_list")

    else:
        form = AttendanceForm()

    return render(
        request,
        "attendance/attendance_form.html",
        {
            "form": form
        }
    )



def attendance_list(request):

    date = request.GET.get('date')

    records = Attendance.objects.all()

    if date:
        records = records.filter(
            date=date
        )

    return render(
        request,
        'attendance/attendance_list.html',
        {
            'records': records
        }
    )