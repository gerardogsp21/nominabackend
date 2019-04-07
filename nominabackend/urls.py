from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('employees.urls')),
    path('', include('payrolls.urls')),
]
