from .models import *
from rest_framework import serializers

class EmployeeSerializer(serializers.ModelSerializer):

    img = serializers.ImageField(required = False)

    class Meta:
        model = Employee
        fields = '__all__'