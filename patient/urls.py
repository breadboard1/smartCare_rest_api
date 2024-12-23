from rest_framework.routers import DefaultRouter
from django.urls import path, include
from . import views

router = DefaultRouter()
router.register('list', views.PatientViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('register/', views.RegistrationViewSet.as_view(), name='register'),
    path('login/', views.LoginViewSet.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('activate/<uid64>/<token>', views.activate, name='activate'),
]