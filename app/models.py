from datetime import datetime
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.
class Setor(models.Model):
    nome = models.CharField(max_length=30)

    def __str__(self):
        return self.nome


class Colaborador(models.Model):
    nome = models.CharField(max_length=50)
    setor = models.ForeignKey(Setor, on_delete=models.CASCADE, null=True, blank=True)
    is_estagiario = models.BooleanField(default=False, verbose_name='Estagiário')

    def __str__(self):
        return self.nome


class PontoDiario(models.Model):
    colaborador = models.ForeignKey(Colaborador, on_delete=models.CASCADE)
    data = models.DateField()
    chegada = models.TimeField()
    saida = models.TimeField()
    tempo_intervalo = models.DurationField(default='1:00:00')
    horas_trabalhadas = models.DurationField(null=True, blank=True)

    def atualizar_horas_trabalhadas(self):
        horas_trabalhadas_delta = datetime.combine(self.data, self.saida) - \
                                  datetime.combine(self.data, self.chegada) - self.tempo_intervalo
        strf_horas_trabalhadas = str(horas_trabalhadas_delta)
        self.horas_trabalhadas = strf_horas_trabalhadas
        PontoDiario.objects.filter(pk=self.pk).update(horas_trabalhadas=strf_horas_trabalhadas)


@receiver(post_save, sender=PontoDiario)
def atualizar_horas_trabalhadas(sender, instance, **kwargs):
    instance.atualizar_horas_trabalhadas()
