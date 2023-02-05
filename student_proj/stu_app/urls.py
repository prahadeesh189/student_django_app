from django.urls import path
from stu_app import views



urlpatterns = [
    path("students", views.studentALL, name="student"),
    path("student/add", views.studentAdd, name="studentAdd"),
    path("student/update", views.studentUpdate, name="studentUpdate"),
    path("student/search/<int:Idnum>", views.studentSearch, name="studentSearch"),

    path("", views.front, name="front")
]