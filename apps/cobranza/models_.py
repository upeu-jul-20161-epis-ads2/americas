# _*_ coding: utf-8 _*_
"""
@copyright   Copyright (c) 2014 Submit Consulting
@author      Angel Sullon (@asullom)
@package     sad
@Descripcion Registro de los modelos de la app

"""
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.text import capfirst, get_text_list
from unicodedata import normalize

# models

# others

N = 'NO'
S = 'SI'
COBRANZA_INTERES_CHOICES = (
    (N, 'NO'),
    (S, 'SI'),
)


class ConceptoCobranza(models.Model):

    class Meta:
        verbose_name = "ConceptoCobranza"
        verbose_name_plural = "ConceptoCobranzas"

    def __str__(self):
        pass


class Cobranza(models.Model):

    """
    Tabla para Cobranza
    """
'''
    concepto_cobranza = models.CharField(
        _('concepto cobranza'),
        max_length=20, null=False, blank=False,
        error_messages={'unique': "eeeee ee"})
'''
    concepto_cobranza = models.ForeignKey(
        ConceptoCobranza, blank=True, null=True)
    importe = models.CharField(
        capfirst(_('importe')), max_length=50, null=False, blank=False)
    detalle = models.TextField(
        capfirst(_('detalle')), max_length=300, null=False, blank=False)
    cobranza_interes = models.CharField(
        _('cobranza interes '),
        max_length=50, choices=COBRANZA_INTERES_CHOICES, default=N)
    fecha_inicio = models.DateField(_('fecha inicio'), null=False, blank=False)
    fecha_fin = models.DateField(_('fecha fin'), null=False, blank=False)

    class Meta:
        verbose_name = _('Cobranza')
        verbose_name_plural = _('Cobranzas')
        unique_together = (
            (
                'concepto_cobranza',
                'importe',
                'detalle',
                'cobranza_interes',
                'fecha_inicio',
                'fecha_fin'
            ))

    def __str__(self):
        cc = self.concepto_cobranza
        i = self.importe
        moneda = 'S/ '
        cadena = "%s %s %s" % (cc, moneda, i)
        return cadena
        # return '%s + %s' % (
        #    self.concepto_cobranza,
        #    self.importe)

    # para el transaction, es necesario poner el
    # transaction.savepoint_rollback(sid)
    def save(self, *args, **kwargs):
        # TODO Mandar con Exception no con ValidationError
        if normalize('NFKD', u'%s %s %s %s %s %s' % (
            self.concepto_cobranza,
            self.importe,
            self.detalle,
            self.cobranza_interes,
            self.fecha_inicio,
            self.fecha_fin
        )).encode('ascii', 'ignore').lower() in list(
                normalize('NFKD', u'%s %s %s %s %s %s' % (
                    c['concepto_cobranza'],
                    c['importe'],
                    c['detalle'],
                    c['cobranza_interes'],
                    c['fecha_inicio'],
                    c['fecha_fin'],
                )).encode(
                    'ascii', 'ignore').lower()
                for c in Cobranza.objects.values(
                    'concepto_cobranza',
                    'importe',
                    'detalle',
                    'cobranza_interes',
                    'fecha_inicio',
                    'fecha_fin'
                ).exclude(pk=self.pk).filter(concepto_cobranza=self.concepto_cobranza)
        ):
            raise Exception(_(u'%(model_name)s with this %(field_label)s already exists.') % {
                'model_name': _('Cobranza'),
                'field_label': get_text_list((
                    capfirst(_('concepto cobranza')),
                    capfirst(_('importe')),
                    capfirst(_('detalle')),
                    capfirst(_('cobranza interes')),
                    capfirst(_('fecha inicio')),
                    capfirst(_('fecha fin'))),
                    _('and')),
            })

        if Cobranza.objects.exclude(id=self.id).filter(concepto_cobranza=self.concepto_cobranza).count() > 0:
            raise Exception(_(u'%(model_name)s with this %(field_label)s already exists.') % {
                'model_name': _('Cobranza'),
                'field_label': get_text_list((capfirst(_('number')),
                                              capfirst(_('Type'))),
                                             _('and')),
            })
        super(Cobranza, self).save(*args, **kwargs)
