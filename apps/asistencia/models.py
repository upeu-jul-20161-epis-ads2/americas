from django.db import models
from apps.params.models import Person

# Create your models here.
class Asistencia(models.Model):

    codigo = models.IntegerField(unique=True)
    nombre = models.CharField(unique=True, max_length=30)
    persona = models.ForeignKey(Person)


    class Meta:
        verbose_name = "Asistencia"
        verbose_name_plural = "Asistencias"

    def __str__(self):
        return self.nombre

S = 'SI'
N = 'NO'
COBRANZA_INTERES_CHOICES = (
    (S, 'SI'),
    (N, 'NO'),
)


