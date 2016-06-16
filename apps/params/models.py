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
from django.dispatch import receiver
from django.db.models import signals
from unicodedata import normalize
from django.core.exceptions import ValidationError
from django.core.exceptions import NON_FIELD_ERRORS

# models

# others

NID = 'NID'
FOREING_CARD = 'FC'
CERTIFICATE_BIRTH = 'CB'
OTHER = 'OTHER'
IDENTITY_TYPE_CHOICES = (
    (NID, _('D.N.I.')),
    (FOREING_CARD, _('CARNE DE EXTRANJERIA')),
    (CERTIFICATE_BIRTH, _('PARTIDA DE NACIMIENTO')),
    (OTHER, _('OTROS')),
)

SELECT_GENDER = 'SG'
H = 'H'
M = 'M'
GENDER_CHOICES = (
    (SELECT_GENDER, 'Seleccione genero'),
    (H, 'Hombre'),
    (M, 'Mujer'),
)


class TipoUsuario(models.Model):

    nombre = models.CharField(max_length=15)

    class Meta:
        verbose_name = "TipoUsuario"
        verbose_name_plural = "TipoUsuarios"

    def __str__(self):
        return self.nombre


class Person(models.Model):

    """
    Tabla para persons
    """

    identity_type = models.CharField(
        _('Identity type'), max_length=10, choices=IDENTITY_TYPE_CHOICES,
        default=NID)
    identity_num = models.CharField(
        _('Identity num'), max_length=20, null=False, blank=False, error_messages={'unique': "eeeee ee"})
    tipo_usuario = models.ForeignKey(TipoUsuario)
    first_name = models.CharField(
        capfirst(_('first name')), max_length=50, null=False, blank=False)
    last_name = models.CharField(
        capfirst(_('last name')), max_length=50, null=False, blank=False)
    domicile = models.CharField(
        capfirst(_('domicile')), max_length=50, null=True, blank=True)
    phone = models.CharField(
        capfirst(_('phone')), max_length=50, null=True, blank=True)
    cell_phone = models.CharField(
        capfirst(_('cell phone')), max_length=50, null=True, blank=True)
    email = models.EmailField(
        capfirst(_('email')),
        unique=True, max_length=50, null=False, blank=False)
    gender = models.CharField(
        _('gender'), max_length=50, choices=GENDER_CHOICES, default=SELECT_GENDER)
    birth_date = models.DateField(_('birth date'), null=True, blank=True)
    photo = models.ImageField(
        _('Photo'), upload_to='persons', default='persons/default.png',
        null=True, blank=True)

    class Meta:
        verbose_name = _('Person')
        verbose_name_plural = _('Persons')
        unique_together = (
            ('first_name', 'last_name', 'identity_type', 'identity_num'),
            ('identity_type', 'identity_num'),
        )


def __str__(self):
    return '%s %s %s' % (self.first_name, self.last_name, self.identity_num)


def save(self, *args, **kwargs):
    # TODO Mandar con Exception no con ValidationError
    if normalize('NFKD', u'%s %s' % (
        self.first_name,
        self.last_name)).encode('ascii', 'ignore').lower() in list(
            normalize('NFKD', u'%s %s' % (
                c['first_name'],
                c['last_name'])).encode(
                'ascii', 'ignore').lower()
            for c in Person.objects.values(
                'first_name',
                'last_name').exclude(pk=self.pk).filter(
                identity_type=self.identity_type,
                identity_num=self.identity_num)
    ):
        raise Exception(_(u'%(model_name)s with this %(field_label)s already exists.') % {
            'model_name': _('Person'),
            'field_label': get_text_list((capfirst(_('first name')),
                                          capfirst(_('last name')),
                                          capfirst(_('number')),
                                          capfirst(_('Type'))),
                                         _('and')),
        })

    if Person.objects.exclude(id=self.id).filter(
            identity_type=self.identity_type,
            identity_num=self.identity_num).count() > 0:
        raise Exception(_(u'%(model_name)s with this %(field_label)s already exists.') % {
            'model_name': _('Person'),
            'field_label': get_text_list((
                capfirst(_('number')),
                capfirst(_('Type'))), _('and')),
        })
    super(Person, self).save(*args, **kwargs)

    '''
    # funciona cunado está con su form, pero Person siempre será llamado desde otro form
    def clean(self):
        raise ValidationError('foo must not be empty')

     # funciona cunado está con su form, pero Person siempre será llamado desde otro form
    def validate_unique(self, exclude=None):

        raise ValidationError(
            {
                NON_FIELD_ERRORS:
                ('Person with same ... already exists.',)
            }
        )

        if normalize("NFKD", u"%s %s" % (self.first_name, self.last_name)).encode("ascii", "ignore").lower() in list(
                normalize("NFKD", u"%s %s" % (c["first_name"], c["last_name"])).encode(
                    "ascii", "ignore").lower()
                for c in Person.objects.values("first_name", "last_name").exclude(pk=self.pk).filter(identity_type=self.identity_type, identity_num=self.identity_num)
        ):
            raise ValidationError({
                'first_name':
                (_(u'%(model_name)s with this %(field_label)s already exists.') % {
                'model_name': _('Person'),
                'field_label': capfirst(_('name')),
                },),
            })

        if Person.objects.exclude(id=self.id).filter(identity_type=self.identity_type, identity_num=self.identity_num).count() > 0:
            raise ValidationError({
                'identity_num':
                (_(u'%(model_name)s with this %(field_label)s already exists.xxx') % {
                'model_name': _('Person'),
                'field_label': get_text_list((capfirst(_('number')), capfirst(_('Type'))), _('and')),
                },),
            })

        return super(Person, self).validate_unique(exclude=exclude)
    '''
