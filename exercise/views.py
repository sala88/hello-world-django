from django.views.decorators.http import require_http_methods
from django.http import HttpResponse
from django.shortcuts import render


@require_http_methods(["GET"])
def index(request):
    return HttpResponse("Hello, world!")


@require_http_methods(["GET"])
def dashboard(request):
    return render(request, "dashboard.html")