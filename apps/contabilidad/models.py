from django.db import models

# Create your models here.


class Ingreso(models.Model):

    codigo = models.IntegerField(unique=True)
    nombre = models.CharField(max_length=20, null=True, blank=True)
    monto = models.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        verbose_name = "Ingreso"
        verbose_name_plural = "Ingresos"

    def __str__(self):
        return '%s %s %s %s' % (self.codigo,
                                self.nombre,
                                self.monto)


class Egreso(models.Model):

    codigo = models.IntegerField(unique=True)
    nombre = models.CharField(max_length=20, null=True, blank=True)
    monto = models.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        verbose_name = "Egreso"
        verbose_name_plural = "Egresos"

    def __str__(self):
        return '%s %s %s %s' % (self.codigo,
                                self.nombre,
                                self.monto)
