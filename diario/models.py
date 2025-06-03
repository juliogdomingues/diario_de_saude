from django.db import models

class Sintoma(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True)
    data = models.DateField()
    horario = models.TimeField()

    def __str__(self):
        return f"{self.nome} ({self.data} {self.horario})"

class Tratamento(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True)
    data_inicio = models.DateField()
    data_fim = models.DateField()

    def __str__(self):
        return self.nome