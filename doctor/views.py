from django.shortcuts import render
from rest_framework import viewsets, pagination, filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from . import models
from . import serializer

# Create your views here.
class DoctorPagination(pagination.PageNumberPagination):
    page_size = 1
    page_size_query_param = page_size


class DoctorViewSet(viewsets.ModelViewSet):
    queryset = models.Doctor.objects.all()
    serializer_class = serializer.DoctorSerializer
    pagination_class = DoctorPagination

class SpecializationViewSet(viewsets.ModelViewSet):
    queryset = models.Specialization.objects.all()
    serializer_class = serializer.SpecializationSerializer

class DesignationViewSet(viewsets.ModelViewSet):
    queryset = models.Designation.objects.all()
    serializer_class = serializer.DesignationSerializer


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = models.Review.objects.all()
    serializer_class = serializer.ReviewSerializer


class AvailableTimeForSpecificDoctor(filters.BaseFilterBackend):
    def filter_queryset(self, request, query_set, view):
        doctor_id = request.query_params.get("doctor_id")
        if doctor_id:
            return query_set.filter(doctor=doctor_id)
        return query_set

class AvailableTimeViewSet(viewsets.ModelViewSet):
    permissions_classes = [IsAuthenticatedOrReadOnly]
    queryset = models.AvailableTime.objects.all()
    serializer_class = serializer.AvailableTimeSerializer
    filter_backends = [AvailableTimeForSpecificDoctor]