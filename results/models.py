from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Student(models.Model):
    #student details
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    reg_number = models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    course=models.CharField(max_length=100)
    year_of_study=models.CharField(max_length=10)
    Session=models.CharField(max_length=10)
    
class Unit(models.Model):
    #unit details
    name = models.CharField(max_length=100)
    unit_code=models.CharField(max_length=30)
    unit_lecturer=models.CharField(max_length=100)
    

class Result(models.Model):
    #result details
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)
    marks = models.DecimalField(max_digits=5, decimal_places=2)
    exam_type=models.CharField(max_length=50)
    exam_date=models.DateField()



