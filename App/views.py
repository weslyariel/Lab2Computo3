from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from . import models
from .models import reservacion
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError


# Create your views here.
@login_required
def index(request):
    return render(request,"inicio.html")

def base(request):
    return render(request,"base.html")

def form_reservacion(request):
    return render(request,"reservacion.html")

def postreservacion(request):
    nom = request.POST.get('nombre')
    corr = request.POST.get('correo')
    tel = request.POST.get('telefono')
    fech = request.POST.get('fecha')
    hor = request.POST.get('hora')
    servici = request.POST.get('servicio')

    # Si el usuario está logeado, guarda la cita con su usuario
    if request.user.is_authenticated:
        usuario = request.user
    else:
        # Si no está logeado, no se asocia un usuario
        usuario = None

    #if not tel.isdigit():
     #   messages.error(request, "El número de teléfono debe contener solo dígitos.")
      #  return redirect('reservacion')  # Redirige de vuelta al formulario

    models.reservacion.objects.create(
        usuario=usuario,  # Aquí asociamos al usuario
        nombre = nom,
        correo = corr,
        telefono = tel,
        fecita = fech,
        hora = hor,
        servicio = servici
    )
    if request.user.is_authenticated:
        messages.success(request, "Reservación guardada exitosamente.")
        return redirect('inicio')  # Redirige a la página "inicio" si el usuario está logeado
    else:
        messages.success(request, "Reservación guardada exitosamente. Por favor, inicia sesión para acceder a más funcionalidades.")
        return redirect('index') # Redirige a la página de registro si no está autenticado

def editar_reservacion(request, id):
    reserva = reservacion.objects.get(id=id)
    
    if request.method == 'POST':
        reserva.nombre = request.POST.get('nombre')
        reserva.correo = request.POST.get('correo')
        reserva.telefono = request.POST.get('telefono')
        reserva.fecita = request.POST.get('fecha')
        reserva.hora = request.POST.get('hora')
        reserva.servicio = request.POST.get('servicio')
        reserva.save()
        messages.success(request, "Reservación actualizada exitosamente.")
        return redirect('recordatorios')
    
    return render(request, 'editar_reservacion.html', {'reserva': reserva})

def eliminar_reservacion(request, id):
    reserva = reservacion.objects.get(id=id)
    reserva.delete()
    return redirect('recordatorios')

def confirmar_asistencia(request, reserva_id):
    # Buscar la reservación por ID
    reserva = get_object_or_404(reservacion, id=reserva_id)
    # Actualizar el estado de confirmación
    reserva.confirmada = True
    reserva.save()
    # Redirigir al usuario nuevamente a los recordatorios
    return redirect('recordatorios')

@login_required
def promociones(request):
    return render(request,"promociones.html")

@login_required
def recordatorios(request):
    # Filtra las reservaciones solo para el usuario autenticado
    reservaciones = reservacion.objects.filter(usuario=request.user)
    # Pasar las reservaciones al contexto
    return render(request, "recordatorios.html", {"reservaciones": reservaciones})
    #return render(request,"recordatorios.html")

"""def inicio(request):
    return render(request,"inicio.html")"""

def registro_usuario(request):
    if request.method == 'POST':
        # Obtiene los datos del formulario
        nombre = request.POST.get('nombre')
        correo = request.POST.get('correo')
        contraseña = request.POST.get('contraseña')
        confirm_contra = request.POST.get('confirm_contra')

        # Verifica que las contraseñas coincidan
        if contraseña != confirm_contra:
            messages.error(request, 'Las contraseñas no coinciden.')
            return render(request, 'index.html')  # Vuelve a renderizar el formulario

        # Verifica si el usuario ya existe
        if User.objects.filter(username=nombre).exists():
            messages.error(request, 'El nombre de usuario ya está en uso.')
            return render(request, 'index.html')  # Vuelve a renderizar el formulario
        elif User.objects.filter(email=correo).exists():
            messages.error(request, 'El correo ya está registrado.')
            return render(request, 'index.html')  # Vuelve a renderizar el formulario
        else:
            # Crea el usuario
            user = User.objects.create_user(username=nombre, email=correo, password=contraseña)
            user.save()
            messages.success(request, '¡Usuario registrado exitosamente!')

            # Redirige al login después de registrar
            return redirect('login')  # Redirige a la página de login

    return render(request, 'index.html')  # Si es un GET, renderiza el formulario


def inicio_sesion(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        contraseña = request.POST.get('contraseña')
        user = authenticate(request, username=nombre, password=contraseña)

        if user is not None:
            login(request, user)
            messages.success(request, 'Inicio de sesión exitoso.')
            return redirect('inicio')  # Redirige a una página después del login
        else:
            messages.error(request, 'Credenciales inválidas.')
    return render(request, 'login.html')

def cerrar_sesion(request):
    logout(request)
    messages.success(request, 'Sesión cerrada correctamente.')
    return redirect('login')    