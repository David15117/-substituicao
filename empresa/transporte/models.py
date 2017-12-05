# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Departamento(models.Model):
    nome=models.CharField(max_length=128)
    def __str__(self):
        return '{}'.format(self.nome)
class Funcionario(models.Model):
    user=models.OneToOneField(User, null=True, blank=False)
    departamento=models.ForeignKey(Departamento, related_name = 'nome_departamento', null = True, blank = False)
    nome=models.CharField(max_length=128)
    cpf=models.CharField(max_length=128)
    def __str__(self):
        return '{}'.format(self.nome)
class Motorista(models.Model):
    nome=models.CharField(max_length=128)
    cpf=models.CharField(max_length=128)
    cnh=models.CharField(max_length=128)
    def __str__(self):
        return self.nome + " ( " + self.cnh + " )"
class Carro(models.Model):
    placa=models.CharField(max_length=128)
    chassi=models.CharField(max_length=128)
    def __str__(self):
        return self.placa+ " ( " + self.chassi + " )"
class DepartamentoSocitacao(models.Model):
    funcionario=models.ManyToManyField(Funcionario, blank=False)
    ##funcionario=models.ForeignKey(Funcionario, related_name = 'motorista', null = True, blank = False)
    ##Existe essas duas maneiras de fazer por Many ou  ForeignKey
    datahora=models.DateTimeField()
    origem=models.CharField(max_length=128)
    destino=models.CharField(max_length=128)
    def __str__(self):
        return self.origem+ " ( " + self.destino + " )"
class AtenderSolicita(models.Model):
    motorista=models.ForeignKey(Motorista, related_name = 'motorista', null = True, blank = False)
    carro=models.ForeignKey(Carro, related_name = 'veiculo', null = True, blank = False)
    departamento=models.ForeignKey(DepartamentoSocitacao, related_name = 'departamento_socilitar', null = True, blank = False)
    def __str__(self):
        return '{}'.format(self.departamento)