from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_preloader, name='index_preloader'), # La raíz ahora es el preloader
    path('home/', views.home, name='home'),
    path('tours/', views.tours, name='tours'),
    path('discografia/', views.discografia, name='discografia'),
    path('galeria/', views.galeria, name='galeria'), 
    path('booking/', views.booking, name='booking'),
]