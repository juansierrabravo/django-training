from django.urls import path

from apps.academy import views

app_name = "academy"

urlpatterns = [
    path("", views.home, name="home"),
    path("student/create/", views.student_info, name="student_info"),
    path("student/assignments/", views.assignments, name="assignments"),
]
