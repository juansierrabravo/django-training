from django import forms
from django.core.exceptions import ValidationError

from apps.academy import models
from apps.utils import helpers


class StudentForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["identifier"].widget.attrs.update(
            {
                "class": "form-control",
                "style": "background-color: var(--third-color); border-color: black;",
            }
        )
        self.fields["name"].widget.attrs.update(
            {
                "class": "form-control",
                "style": "background-color: var(--third-color); border-color: black;",
            }
        )
        self.fields["phone"].widget.attrs.update(
            {
                "class": "form-control",
                "style": "background-color: var(--third-color); border-color: black;",
            }
        )

    class Meta:
        model = models.Student
        fields = ("identifier", "name", "phone")

    def clean_name(self):
        """Validate if the name does not have numbers"""

        name = self.cleaned_data["name"]
        if helpers.has_numbers(name):
            raise ValidationError("The name cannot contain numbers")

        return name

    def clean_phone(self):
        """Validate if the phone has exactly 10 digits"""

        phone = self.cleaned_data["phone"]
        if len(str(phone)) != 10:
            raise ValidationError("The phone must have 10 digits")

        return phone


class StudentAssignmentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["student"].widget.attrs.update(
            {
                "class": "form-control",
                "style": "background-color: var(--third-color); border-color: black;",
            }
        )
        self.fields["assignment"].widget.attrs.update(
            {
                "class": "form-control",
                "style": "background-color: var(--third-color); border-color: black;",
            }
        )

    class Meta:
        model = models.StudentAssignment
        fields = ("student", "assignment")
