from django.shortcuts import render, redirect
from .forms import GradeForm
from .models import Grade


def grade_create(request):

    if request.method == "POST":

        form = GradeForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('grade_list')

    else:
        form = GradeForm()

    return render(
        request,
        'grades/grade_form.html',
        {'form': form}
    )


def grade_list(request):

    grades = Grade.objects.all()

    return render(
        request,
        'grades/grade_list.html',
        {'grades': grades}
    )