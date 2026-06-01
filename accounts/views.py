from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from students.models import Student


def user_login(request):

    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            login(request, user)
            return redirect("dashboard")

    return render(request, "accounts/login.html")


@login_required
def dashboard(request):

    student_count = Student.objects.count()

    if request.user.role == "admin":
        return render(
            request,
            "accounts/admin_dashboard.html",
            {
                "student_count": student_count
            }
        )

    elif request.user.role == "teacher":
        return render(
            request,
            "accounts/teacher_dashboard.html"
        )

    elif request.user.role == "student":
        return render(
            request,
            "accounts/student_dashboard.html"
        )

    return redirect("login")


def user_logout(request):
    logout(request)
    return redirect("login")