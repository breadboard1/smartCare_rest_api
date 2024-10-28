from rest_framework.routers import DefaultRouter
from django.urls import path, include
from . import views

router = DefaultRouter()
router.register('list', views.DoctorViewSet)
router.register('specialization', views.SpecializationViewSet)
router.register('designation', views.DesignationViewSet)
router.register('review', views.ReviewViewSet)
router.register('available_time', views.AvailableTimeViewSet)


urlpatterns = [
    path('', include(router.urls)),
]