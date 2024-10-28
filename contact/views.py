from django.shortcuts import render
from rest_framework import viewsets
from . import models
from . import serializer

# Create your views here.
class ContactViewSet(viewsets.ModelViewSet):
    queryset = models.Contact.objects.all()
    serializer_class = serializer.ContactSerializer