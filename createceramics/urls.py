from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/<int:pk>/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('booknow/', views.booknow, name='booknow'),
    path('mybookings/', views.mybookings, name='mybookings'),
]