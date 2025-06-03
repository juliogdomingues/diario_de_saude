from django.db import models
from django.contrib.auth.models import User

class Sintoma(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    data = models.DateField()

    def __str__(self):
        return self.titulo

class Tratamento(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    data = models.DateField()

    def __str__(self):
        return self.titulo