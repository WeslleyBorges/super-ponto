from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Colaborador)
class ColadoradorAdmin(admin.ModelAdmin):
    list_display = ('nome', 'setor',)


@admin.register(PontoDiario)
class PontoDiarioAdmin(admin.ModelAdmin):
    list_display = ('colaborador', 'data', 'chegada', 'saida', 'horas_trabalhadas',)
    list_filter = ('data', 'colaborador',)


@admin.register(Setor)
class Setor(admin.ModelAdmin):
    pass
