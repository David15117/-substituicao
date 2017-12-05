# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework import routers, serializers, viewsets
from django.shortcuts import render
from django.http import HttpResponse
from transporte.models import *
from transporte.serializers import *

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
class DepartamentoViewSet(viewsets.ModelViewSet):
    queryset = Departamento.objects.all()
    serializer_class = DepartamentoSerializer
class CarroViewSet(viewsets.ModelViewSet):
    queryset = Carro.objects.all()
    serializer_class = CarroSerializer
class MotoristaViewSet(viewsets.ModelViewSet):
    queryset = Motorista.objects.all()
    serializer_class = MotoristaSerializer
class FuncionarioViewSet(viewsets.ModelViewSet):
    queryset = Funcionario.objects.all()
    serializer_class = FuncionarioSerializer
class DepartamentoSocitacaoViewSet(viewsets.ModelViewSet):
    queryset = DepartamentoSocitacao.objects.all()
    serializer_class = DepartamentoSocitacaoSerializer
class AtenderSolicitaViewSet(viewsets.ModelViewSet):
    queryset = AtenderSolicita.objects.all()
    serializer_class = AtenderSolicitaSerializer
    
