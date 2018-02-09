from django.shortcuts import render, redirect
from django.views.generic.base import View
from usuarios.forms import RegistrarUsuarioForm
from django.contrib.auth.models import User
from contas.models import Conta

class RegistrarUsuarioView(View):

    template_name = 'registrar.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        form = RegistrarUsuarioForm(request.POST)
        if form.is_valid():
            dados_form = form.data

            usuario = User.objects.create_user(dados_form['numero'], dados_form['titular'], dados_form['cpf'], dados_form['senha'])
            conta = Conta(numero=dados_form['numero'],
                            titular=dados_form['titular'],
                            cpf=dados_form['cpf'],
                            saldo=dados_form['saldo'],
                            limite=1000.0,
                            usuario=usuario)
            conta.save()
            return redirect('index')

        return render(request, self.template_name, {'form': form })
