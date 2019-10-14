from django.db import models

class Student(models.Model):
    registration = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    absence_number = models.IntegerField()