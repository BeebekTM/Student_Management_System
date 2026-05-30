from django.shortcuts import render
from .models import Student

def student_list(request):
    students = Student.objects.all()

    print(students)  # DEBUG (important)

    return render(request, 'students/student_list.html', {
        'students': students
    })