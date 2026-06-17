from django.shortcuts import render, redirect, get_object_or_404
from django.core.mail import send_mail

from .models import Student
from .form import StudentForm


def student_list(request):

    query = request.GET.get('q')

    students = Student.objects.all()

    if query:
        students = students.filter(
            name__icontains=query
        )

    return render(
        request,
        'students/student_list.html',
        {
            'students': students
        }
    )


def student_create(request):

    if request.method == 'POST':

        form = StudentForm(request.POST)

        if form.is_valid():

            student = form.save()

            send_mail(
                subject='Welcome to SMS',
                message=f'Hello {student.name}, welcome to Student Management System.',
                from_email='admin@sms.com',
                recipient_list=[student.email],
                fail_silently=False,
            )

            return redirect('student_list')

    else:
        form = StudentForm()

    return render(
        request,
        'students/student_form.html',
        {
            'form': form
        }
    )


def student_update(request, pk):

    student = get_object_or_404(
        Student,
        pk=pk
    )

    if request.method == 'POST':

        form = StudentForm(
            request.POST,
            instance=student
        )

        if form.is_valid():
            form.save()
            return redirect('student_list')

    else:

        form = StudentForm(
            instance=student
        )

    return render(
        request,
        'students/student_form.html',
        {
            'form': form
        }
    )


def student_delete(request, pk):

    student = get_object_or_404(
        Student,
        pk=pk
    )

    if request.method == 'POST':

        student.delete()

        return redirect(
            'student_list'
        )

    return render(
        request,
        'students/student_confirm_delete.html',
        {
            'student': student
        }
    )