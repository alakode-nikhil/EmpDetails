from django.shortcuts import render
from rest_framework import generics,permissions
from .models import *
from .serializers import *

# Create your views here.
class CreateEmployeeApi(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [permissions.AllowAny]

class RetrieveEmployeeApi(generics.RetrieveAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class UpdateEmployeeApi(generics.RetrieveUpdateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class SearchEmployeeApi(generics.ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    def get_queryset(self):
        employee_name = self.kwargs.get('employee')
        return Employee.objects.filter(name__icontains = employee_name)
    
class DeleteEmployeeApi(generics.DestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
