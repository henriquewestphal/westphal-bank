# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Conta(models.Model):
    numero = models.CharField(max_length=255, null=False)
    titular = models.CharField(max_length=255, null=False)
    cpf = models.CharField(max_length=11, null=False)
    saldo = models.DecimalField(max_digits=10000, decimal_places=0, null=False)
    limite = models.DecimalField(max_digits=10000, decimal_places=0, null=False)

    def convidar(self, conta_convidado):
        pass
