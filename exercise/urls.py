from django.urls import path
from . import views

urlpatterns = [
    path("", views.dashboard, name="dashboard"),
    path("students", views.students, name="students"),
    path("doubleaverage", views.doubleaverage, name="doubleaverage")

]