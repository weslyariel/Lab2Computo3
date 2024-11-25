"""
URL configuration for ProyectoProgra_III project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from App import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index), 
    path('index/', views.index, name='inicio'),
    path('base/', views.base),
    path('reservacion/', views.form_reservacion, name='reservacion'),
    path('promociones/', views.promociones, name='promociones'),
    path('recordatorios/',views.recordatorios, name='recordatorios'),
    
    path('postreservacion/', views.postreservacion),
    path('editar_reservacion/<int:id>/', views.editar_reservacion, name='editar_reservacion'),
    path('eliminar_reservacion/<int:id>/', views.eliminar_reservacion, name='eliminar_reservacion'),
    path('confirmar/<int:reserva_id>/', views.confirmar_asistencia, name='confirmar_asistencia'),
    path('registro/', views.registro_usuario, name='index'),
    path('login/', views.inicio_sesion, name='login'),
    path('logout/', views.cerrar_sesion, name='logout'),
]
