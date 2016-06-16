from django.db import models
# from django.utils.translation import ugettext_lazy as _
# from django.utils.text import capfirst, get_text_list
# from unicodedata import normalize


class Concepto(models.Model):

    codigo = models.IntegerField(unique=True)
    nombre = models.CharField(unique=True, max_length=30)

    class Meta:
        verbose_name = "Concepto"
        verbose_name_plural = "Conceptos"

    def __str__(self):
        return self.nombre

S = 'SI'
N = 'NO'
COBRANZA_INTERES_CHOICES = (
    (S, 'SI'),
    (N, 'NO'),
)


class Moneda(models.Model):

    codigo = models.IntegerField(unique=True)
    nombre = models.CharField(unique=True, max_length=10)
    simbolo = models.CharField(unique=True, max_length=5)

    class Meta:
        verbose_name = "Moneda"
        verbose_name_plural = "Monedas"

    def __str__(self):
        return self.nombre


class ImporteInter(models.Model):

    codigo = models.IntegerField(unique=True)
    importe = models.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        verbose_name = "ImporteInter"
        verbose_name_plural = "ImporteInters"

    def __str__(self):
        pass


class Deuda(models.Model):

    concepto_deuda = models.ForeignKey(
        Concepto, blank=False, null=False)
    moneda = models.ForeignKey(Moneda, blank=False, null=False)
    importe = models.DecimalField(max_digits=5, decimal_places=2)
    detalle = models.TextField(max_length=50, null=True, blank=True)
    cobranza_interes = models.CharField(
        max_length=50, choices=COBRANZA_INTERES_CHOICES, default=N)
    fecha_inicio = models.DateField(null=True, blank=True)
    fecha_fin = models.DateField(null=True, blank=True)

    class Meta:
        verbose_name = "Deuda"
        verbose_name_plural = "Deudas"

    def __str__(self):
        return "%s %s %s" % (self.concepto_deuda, self.importe, self.moneda)
