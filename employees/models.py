from django.db import models

class Employee(models.Model):
	numero_identificacion = models.CharField(max_length=15)
	nombres = models.CharField(max_length=50)
	apellidos = models.CharField(max_length=50)
	cargo = models.CharField(max_length=100)
	salario = models.CharField(max_length=10)
	create_at = models.DateTimeField(auto_now_add=True)
		
