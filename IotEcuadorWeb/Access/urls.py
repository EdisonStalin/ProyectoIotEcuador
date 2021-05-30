from django.urls import path
from Access import views

urlpatterns = [
    path('', views.home, name="Inicio"),
    path('dashboard', views.dashboard, name="Dashboard"),
    path('busqueda', views.search, name="Search"),
    path('registro', views.register, name="Register"),
]