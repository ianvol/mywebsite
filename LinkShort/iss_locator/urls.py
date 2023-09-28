from django.urls import path
from . import views

app_name = 'iss_locator'

urlpatterns = [
    path('iss/', views.iss, name='iss'),
    path('iss/get_position/', views.get_iss_position, name='get_iss_position'),
]
