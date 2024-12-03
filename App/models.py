from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User

# Create your models here.

class reservacion(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    nombre = models.CharField(max_length=100)
    correo = models.CharField(max_length=110)
    telefono = models.CharField(max_length=15)
    fecita = models.DateField()
    hora = models.TimeField()
    confirmada = models.BooleanField(default=False)  # Nuevo campo
    servicio = models.CharField(
        max_length=20,
        choices=[
            ('consulta', 'Consulta'),
            ('seguimiento', 'Seguimiento'),
            ('evaluacion', 'Evaluación'),
        ],
    )
    def clean(self):
        if not self.telefono.isdigit():
            raise ValidationError("El número de teléfono debe contener solo dígitos.")

    def __str__(self):
        return ("Cita de: "  + self.nombre )