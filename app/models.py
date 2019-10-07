from django.db import models


# Create your models here.
class Setor(models.Model):
    nome = models.CharField(max_length=30)

    def __str__(self):
        return self.nome


class Colaborador(models.Model):
    nome = models.CharField(max_length=50)
    setor = models.ForeignKey(Setor, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome


class Ponto(models.Model):
    colaborador = models.ForeignKey(Colaborador, on_delete=models.CASCADE)
    data = models.DateField()
    chegada = models.TimeField()
    saida = models.TimeField()
    tempo_intervalo = models.DurationField()

    def __str__(self):
        return '%s - %s' % (self.colaborador, self.data)


