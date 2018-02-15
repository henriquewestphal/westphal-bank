from django import forms

class MudaSaldoForm(forms.Form):
    valor = forms.FloatField(required=True)


#        def saque(self, valor):
#            self.saldo = self.saldo-valor.save()

#            return render(request, 'conta.html')

#        def depositar(self, valor):
#            self.saldo = self.saldo+valor.save()

#            return render(request, 'conta.html')
