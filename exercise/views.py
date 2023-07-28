from django.views.decorators.http import require_http_methods
from django.shortcuts import render
from .models import Student
from django.db.models import F


@require_http_methods(["GET"])
def dashboard(request):
    return render(request, "dashboard.html")

@require_http_methods(["GET", "POST"])
def students(request):
    if request.method == "POST":
        student = Student(first_name=request.POST['first_name'], last_name=request.POST['last_name'], course=request.POST['course'], average=request.POST['average'])
        student.save()

    students = Student.objects.all()
    return render(request, "students.html", {'students': students})


@require_http_methods(["GET"])
def doubleaverage(request):
    student = Student.objects.get(first_name="Mario")
    student.average = F("average") * 2
    student.save()
    students = Student.objects.all()
    return render(request, "students.html", {'students': students})
