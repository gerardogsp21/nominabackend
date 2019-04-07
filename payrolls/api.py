from payrolls.models import Payroll
from rest_framework import viewsets, permissions
from .serializers import PayrollSerializer

# Payroll ViewSet

class PayrollViewSet(viewsets.ModelViewSet):
	queryset = Payroll.objects.all()
	permission_classes = [
		permissions.AllowAny
	]
	serializer_class = PayrollSerializer