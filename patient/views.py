from django.shortcuts import render
from rest_framework import viewsets
from . import models
from . import serializer

# Create your views here.
class PatientViewSet(viewsets.ModelViewSet):
    queryset = models.Patient.objects.all()
    serializer_class = serializer.PatientSerializer