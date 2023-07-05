from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('room/<int:pk>/', views.room, name='room'),
    path('services/', views.services, name='services'),
    path('booknow/', views.booknow, name='booknow'),
]