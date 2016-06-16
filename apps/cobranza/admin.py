from django.contrib import admin

# Register your models here.
from .models import Concepto, Moneda, Deuda
admin.site.register(Concepto)
admin.site.register(Moneda)
admin.site.register(Deuda)
