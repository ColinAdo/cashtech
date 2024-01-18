from django.urls import path

from .import views

urlpatterns = [
    path('', views.account, name='account'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('kyc-reg/', views.kyc_registration, name='kyc'),
]