from django.db import models

# Create your models here.

class reservacion(models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.CharField(max_length=110)
    telefono = models.IntegerField()
    fecita = models.DateField()
    hora = models.TimeField()
    ampm = models.CharField(max_length=2, choices=[('AM', 'AM'), ('PM', 'PM')])
    confirmada = models.BooleanField(default=False)  # Nuevo campo
    servicio = models.CharField(
        max_length=20,
        choices=[
            ('consulta', 'Consulta'),
            ('seguimiento', 'Seguimiento'),
            ('evaluacion', 'Evaluación'),
        ],
    )

    def __str__(self):
        return ("Cita de " + self.nombre)