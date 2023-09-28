
from datetime import datetime
from django.urls import path
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from app import views  # Import views from the 'app' directory

urlpatterns = [
    path('', views.me, name='me'),  # The default page
    path('linkshort/', views.link_short, name='link_short'),  # URL for LinkShort functionalities
    path('iss/', views.iss, name='iss'),
    path('my_projects/', views.project_flex, name = 'project_flex'),
    path('redirect/', views.my_links, name='redirect'),  # URL for My Links functionality
    path('redirect/<short_url>', views.redirect_short_url, name='redirect_short_url'),
    path("admin/", admin.site.urls),  # Admin URL
]