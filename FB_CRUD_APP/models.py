from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length = 20,)
    age = models.IntegerField()
    gender_choice = (
        ("M", "Male"),
        ("F", "Female"),
    )
    gender = models.CharField(max_length=11, choices = gender_choice)
    engineering_choice = (
        ("ECE", "Electronics & Communication Engineering"),
        ("CSE", "Computer Science Engineering"),
        ("ME", "Mechanical Engineering"),
        ("CE", "Civil Engineering"),
        ("EEE", "Electrical & Electronics Engineering"),
        ("ISE", "Information Science Engineering"),
        ("AE", "Aeronautical Engineering"),
    )
    engineering_stream = models.CharField(max_length=50, choices = engineering_choice)
    college = models.CharField(max_length=200)
    place = models.CharField(max_length = 50)

    def __str__(self):
        return  self.name

