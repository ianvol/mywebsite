from django.urls import path
from . import views

urlpatterns = [
    path('', views.mastercard_currency_converter, name='mastercard_currency_converter'),
]
