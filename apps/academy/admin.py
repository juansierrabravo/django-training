from django.contrib import admin
from apps.academy import models


admin.site.register(models.Student)
admin.site.register(models.Assignment)
admin.site.register(models.StudentAssignment)
