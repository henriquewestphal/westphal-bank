# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User

class Conta(models.Model):
    numero = models.CharField(max_length=255)
    titular = models.CharField(max_length=255, null=False)
    cpf = models.CharField(max_length=11, null=False)
    saldo = models.FloatField(null=False)
    limite = '1000.0'
    contatos = models.ManyToManyField('self')
    usuario = models.OneToOneField(User, related_name="conta")


    def convidar(self, conta_convidado):
        convite = Convite(solicitante=self, convidado=conta_convidado).save()


class Convite(models.Model):
    solicitante = models.ForeignKey(Conta, related_name='convites_feitos')
    convidado = models.ForeignKey(Conta, related_name='convites_recebidos')

    def aceitar(self):
        self.convidado.contatos.add(self.solicitante)
        self.solicitante.contatos.add(self.convidado)
        self.delete()

    def sacar(self, valor):
        self.saldo = self.saldo-valor.save()
        return

    def depositar(self, valor):

        self.saldo = self.saldo+valor.save()
        return 
