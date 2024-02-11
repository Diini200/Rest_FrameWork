from rest_framework import serializers


class Emp_Serializers(serializers.Serializer):
    Emp_Id = serializers.IntegerField()
    Emp_Name = serializers.CharField(max_length=35)
    Emp_Salary = serializers.IntegerField()
    Emp_Email = serializers.EmailField()
    Emp_Number = serializers.IntegerField()
