from django.forms import ModelForm
from .models import Attendance


class AttendanceForm(ModelForm):

    class Meta:
        model = Attendance
        fields = [
            'student',
            'course',
            'date',
            'status'
        ]