# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from contas.models import Conta


def index(request):
    return render(request, 'index.html',{'contas': Conta.objects.all()})


def exibir(request, conta_id):

    conta = Conta.objects.get(id=conta_id)
    return render(request, 'conta.html', {"conta" : conta})

def convidar(request, conta_id):
    conta_a_convidar = Conta.objects.get(id=conta_id)
    conta_logado = get_conta_logado(request)
    conta_logado.convidar(conta_a_convidar)
    return redirect('index')

def get_conta_logado(request):
    return Conta.objects.get(id=1)
