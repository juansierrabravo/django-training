from django.shortcuts import render, redirect
from django.views.generic import View

from apps.academy import forms


class HomeView(View):
    def get(self, request):
        return render(request, "home.html")


class StudentInfoView(View):
    form_class = forms.StudentForm

    def get(self, request):
        form = self.form_class()
        return render(request, "student_info.html", {"form": form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect("academy:home")
        else:
            return render(request, "student_info.html", {"form": form})


class AssignmentsView(View):
    form_class = forms.StudentAssignmentForm

    def get(self, request):
        form = self.form_class()
        return render(request, "assignments.html", {"form": form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect("academy:home")
        else:
            return render(request, "assignments.html", {"form": form})
