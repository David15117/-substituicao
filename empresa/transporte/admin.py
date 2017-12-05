# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from transporte.models import *
from django.contrib import admin

# Register your models here.
admin.site.register(Funcionario)
admin.site.register(Motorista)
admin.site.register(Carro)
admin.site.register(DepartamentoSocitacao)
admin.site.register(Departamento)
admin.site.register(AtenderSolicita)