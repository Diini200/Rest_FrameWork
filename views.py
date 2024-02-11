from django.shortcuts import render
from Application1.models import Employee
from django.http import HttpResponse
from Application1.serializers import Emp_Serializers
from rest_framework.renderers import JSONRenderer


def EmployeeRecord(request):
    data = Employee.objects.get(Emp_Id="101")
    data_serial = Emp_Serializers(data)
    Json_dat = JSONRenderer().render(data_serial.data)
    return HttpResponse(Json_dat, content_type='application/json')


def Employee_All_Records(request):
    data = Employee.objects.all()
    data_serial = Emp_Serializers(data, many=True)
    Json_dat = JSONRenderer().render(data_serial.data)
    return HttpResponse(Json_dat, content_type='application/json')


def Employee_OneByOne_Record(request, pk):
    data = Employee.objects.get(Emp_Id=pk)
    data_serail = Emp_Serializers(data)
    Json_data = JSONRenderer().render(data_serail.data)
    return HttpResponse(Json_data, content_type='application/json')
