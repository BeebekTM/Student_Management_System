from django.http import HttpResponse
from reportlab.pdfgen import canvas
from students.models import Student


def student_report(request):

    response = HttpResponse(
        content_type='application/pdf'
    )

    response[
        'Content-Disposition'
    ] = 'attachment; filename="students.pdf"'

    pdf = canvas.Canvas(response)

    pdf.drawString(
        100,
        800,
        "Student Report"
    )

    students = Student.objects.all()

    y = 760

    for student in students:

        pdf.drawString(
            100,
            y,
            f"{student.name} - {student.email}"
        )

        y -= 20

    pdf.save()

    return response