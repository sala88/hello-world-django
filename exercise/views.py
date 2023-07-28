from django.views.decorators.http import require_http_methods
from django.shortcuts import render
from .models import Student

@require_http_methods(["GET"])
def dashboard(request):
    return render(request, "dashboard.html")

@require_http_methods(["GET", "POST"])
def students(request):
    if request.method == "POST":
        pass



    else:
        students = Student.objects.all()
        return render(request, "students.html", {'students': students})
