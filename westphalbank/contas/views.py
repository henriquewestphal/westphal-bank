# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from contas.models import Conta


def index(request):
    return render(request, 'index.html')


def exibir(request, conta_id):

    conta = Conta()
    if conta_id == '1':
        conta = Conta('123', 'henrique westphal', "086.198.999-61", "100.0", "1000.0")
    return render(request, 'conta.html')
