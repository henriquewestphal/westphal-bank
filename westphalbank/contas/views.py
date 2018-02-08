# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from contas.models import Conta, Convite


def index(request):
    return render(request, 'index.html',{'contas': Conta.objects.all(), 'conta_logado': get_conta_logado(request)})


def exibir(request, conta_id):
    conta = Conta.objects.get(id=conta_id)
    conta_logado = get_conta_logado(request)
    ja_e_contato = conta in conta_logado.contatos.all()
    return render(request, 'conta.html', {"conta" : conta, 'conta_logado': get_conta_logado(request), 'ja_e_contato': ja_e_contato})

def convidar(request, conta_id):
    conta_a_convidar = Conta.objects.get(id=conta_id)
    conta_logado = get_conta_logado(request)
    conta_logado.convidar(conta_a_convidar)
    return redirect('index')

def get_conta_logado(request):
    return Conta.objects.get(id=1)

def aceitar(request, convite_id):
    convite = Convite.objects.get(id=convite_id)
    convite.aceitar()
    return redirect('index')
