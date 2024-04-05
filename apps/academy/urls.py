from django.urls import path

from apps.academy import views

app_name = "academy"

urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path("student/create/", views.StudentInfoView.as_view(), name="student_info"),
    path("student/assignments/", views.AssignmentsView.as_view(), name="assignments"),
]
