from django.db import models


class Employee(models.Model):
    Emp_Id = models.IntegerField()
    Emp_Name = models.CharField(max_length=35)
    Emp_Salary = models.IntegerField()
    Emp_Email = models.EmailField()
    Emp_Number = models.IntegerField()
