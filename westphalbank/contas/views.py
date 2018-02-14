# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from contas.models import Conta, Convite
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    return render(request, 'index.html',{'contas': Conta.objects.all(), 'conta_logado': get_conta_logado(request)})

@login_required
def exibir(request, conta_id):
    conta = Conta.objects.get(id=conta_id)
    conta_logado = get_conta_logado(request)
    ja_e_contato = conta in conta_logado.contatos.all()
    return render(request, 'conta.html', {"conta" : conta, 'conta_logado': get_conta_logado(request), 'ja_e_contato': ja_e_contato})

@login_required
def convidar(request, conta_id):
    conta_a_convidar = Conta.objects.get(id=conta_id)
    conta_logado = get_conta_logado(request)
    conta_logado.convidar(conta_a_convidar)
    return redirect('index')

@login_required
def get_conta_logado(request):
    return request.user.conta

@login_required
def aceitar(request, convite_id):
    convite = Convite.objects.get(id=convite_id)
    convite.aceitar()
    return redirect('index')

def sacar(request, conta_id):
    conta = Conta.objects.get(id=conta_id)
    return render(request, 'sacar.html')

def depositar(request):
    pass
