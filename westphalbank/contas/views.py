# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from contas.models import Conta


def index(request):
    return render(request, 'index.html')


def exibir(request, conta_id):

    conta = Conta.objects.get(id=conta_id)
    return render(request, 'conta.html', {"conta" : conta})
