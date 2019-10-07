from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Colaborador)
class ColadoradorAdmin(admin.ModelAdmin):
    pass


@admin.register(Ponto)
class PontoAdmin(admin.ModelAdmin):
    pass


@admin.register(Setor)
class Setor(admin.ModelAdmin):
    pass
