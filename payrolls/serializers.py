from rest_framework import serializers
from payrolls.models import Payroll

#Payroll Serializer

class PayrollSerializer(serializers.ModelSerializer):
	class Meta:
		model = Payroll
		fields = '__all__'