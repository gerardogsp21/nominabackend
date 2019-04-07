from django.db import models

class Payroll(models.Model):
	dias_laborados = models.CharField(max_length=3)
	sueldo = models.CharField(max_length=20)
	auxlio_transporte = models.CharField(max_length=20)
	total_devengado = models.CharField(max_length=20)
	salud = models.CharField(max_length=20)
	pension = models.CharField(max_length=20)
	fsp = models.CharField(max_length=20)
	total_deducido = models.CharField(max_length=20)
	neto_pagar = models.CharField(max_length=20)
	empleado_id = models.CharField(max_length=20)
		
