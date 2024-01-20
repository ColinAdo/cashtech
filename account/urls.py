from django.urls import path

from .import views

urlpatterns = [
    path('', views.account, name='account'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('kyc-reg/', views.kyc_registration, name='kyc'),
    path('card_detail/<credit_id>/', views.card_detail, name='card_detail'),
    path('fund-card/<credit_id>/', views.fund_credit_card, name='fund_credit_card'),
]