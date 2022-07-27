from django.contrib import admin

# Register your models here.
from .models import Student




# @admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "age", "gender", "engineering_stream", "college", "place"]


admin.site.register(Student, StudentAdmin)