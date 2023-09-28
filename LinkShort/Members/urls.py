from django.contrib import admin
from django.urls import include, path
from . import views


urlpatterns = [
    path('authenticate/login/', views.user_login, name="login"),
    path('authenticate/register/', views.register, name='register'),
    path('logout/', views.logout_user, name='logout'),
]



