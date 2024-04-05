from django.shortcuts import render, redirect
from django.http import HttpResponseNotAllowed

from apps.academy import forms


def home(request):
    if request.method == "GET":
        return render(request, "home.html")
    else:
        return HttpResponseNotAllowed(["GET"])


def student_info(request):
    if request.method == "GET":
        form = forms.StudentForm()
        return render(request, "student_info.html", {"form": form})

    if request.method == "POST":
        form = forms.StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("academy:home")
        else:
            return render(request, "student_info.html", {"form": form})

    return HttpResponseNotAllowed(["GET", "POST"])


def assignments(request):
    if request.method == "GET":
        form = forms.StudentAssignmentForm()
        return render(request, "assignments.html", {"form": form})

    if request.method == "POST":
        form = forms.StudentAssignmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("academy:home")
        else:
            return render(request, "assignments.html", {"form": form})

    return HttpResponseNotAllowed(["GET", "POST"])
