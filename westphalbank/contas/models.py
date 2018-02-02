# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Conta(object):
    """docstring for Conta."""
    def __init__(self, numero='', titular='', cpf='', saldo='', limite=''):

        self.numero = numero
        self.titular = titular
        self.cpf = cpf
        self.saldo = saldo
        self.limite = limite
