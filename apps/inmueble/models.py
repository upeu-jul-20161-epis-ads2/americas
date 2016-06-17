from django.db import models
from django.utils.translation import ugettext_lazy as _
# from django.utils.text import capfirst, get_text_list
# from django.dispatch import receiver
# from django.db.models import signals
# from unicodedata import normalize
# from django.core.exceptions import ValidationError
# from django.core.exceptions import NON_FIELD_ERRORS

from apps.params.models import Person
# Create your models here.


class Lote(models.Model):

    codigo = models.IntegerField(unique=True)
    numero_lote = models.CharField(max_length=50, null=True, blank=True)
    propietario = models.ForeignKey(Person)
    ubizacion = models.CharField(
        max_length=15, unique=True, null=False, blank=False)
    area_terreno = models.DecimalField(max_digits=5, decimal_places=2)
    estado_construccion = models.CharField(
        max_length=50, null=True, blank=True)
    foto = models.ImageField(
        _('foto'), upload_to='lotes', default='lotes/default.png',
        null=True, blank=True)

    class Meta:
        verbose_name = "Lote"
        verbose_name_plural = "Lotes"

    def __str__(self):
        return '%s %s %s %s' % (
            self.numero_lote, self.propietario,
            self.ubizacion, self.area_terreno)
