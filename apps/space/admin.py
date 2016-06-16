# _*_ coding: utf-8 _*_
from django.contrib import admin
# from django import forms
# from django.utils.translation import ugettext_lazy as _

# models
from .models import Solution, EntidadBancaria, Enterprise
from .models import Cuenta, Association, Headquar


class SolutionAdmin(admin.ModelAdmin):

    """docstring for SolutionAdmin"""
    # formfield_overrides = {
    #    models.ManyToManyField: {'widget': CheckboxSelectMultiple},
    # }

    list_display = ('name', 'description', 'is_active',)
    search_fields = ('name', 'is_active',)
    list_per_page = 2


class CuentaAdmin(admin.ModelAdmin):

    list_display = ('nombre', )
    search_fields = ('nombre', 'codigo',)
    list_per_page = 10


class EntidadBancariaAdmin(admin.ModelAdmin):

    list_display = ('nombre', )
    search_fields = ('codigo', 'nombre', 'entidad_bancaria', 'numero_cuenta', )
    list_per_page = 10


class EnterpriseAdmin(admin.ModelAdmin):

    list_display = ('name', 'cuenta_bancaria',
                    'tax_id', 'type_e', 'is_active', 'solution',)
    search_fields = ('name', 'cuenta_bancaria',
                     'tax_id', 'type_e', 'is_active', 'solution', )
    list_per_page = 10


class AssociationAdmin(admin.ModelAdmin):

    list_display = ('name', 'type_a', 'is_active', 'is_actived', 'solution', )
    search_fields = ('name', 'type_a', 'is_active', 'is_actived', 'solution', )
    list_per_page = 10


class HeadquarAdmin(admin.ModelAdmin):

    list_display = ('name', 'phone', 'address', 'is_main',
                    'is_active', 'is_actived', 'association', 'enterprise', )
    search_fields = ('name', 'phone', 'address', 'is_main', )
    list_per_page = 10

admin.site.register(Solution, SolutionAdmin)
admin.site.register(EntidadBancaria, EntidadBancariaAdmin)
admin.site.register(Cuenta, CuentaAdmin)
admin.site.register(Enterprise, EnterpriseAdmin)
admin.site.register(Association, AssociationAdmin)
admin.site.register(Headquar, HeadquarAdmin)
