from django.urls import path
from Access import views

urlpatterns = [
    path('', views.home, name="Inicio"),
    path('dashboard', views.dashboard, name="Dashboard"),
    path('search', views.search, name="Busqueda"),
    path('register', views.register, name="Registro"),
]