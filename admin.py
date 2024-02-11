from django.contrib import admin
from Application1.models import Employee


class Emp_Admin(admin.ModelAdmin):
    list_display = ['Emp_Id', 'Emp_Name',
                    'Emp_Salary', 'Emp_Email', 'Emp_Number']


admin.site.register(Employee, Emp_Admin)
