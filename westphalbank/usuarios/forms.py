from django import forms
from django.contrib.auth.models import User

class RegistrarUsuarioForm(forms.Form):
    numero = forms.DecimalField(required=False)
    titular = forms.CharField(required=True)
    cpf = forms.CharField(required=True)
    saldo = forms.FloatField(required=True)
    senha = forms.CharField(required=True)

    def is_valid(self):
        valid = True
        if not super(RegistrarUsuarioForm, self).is_valid():
            self.adiciona_erro('Por Favor verifique os dados informados')
            valid = False
        user_exists = User.objects.filter(username=self.data['titular']).exists()

        if user_exists:
            self.adiciona_erro('Usuario ja existente')
            valid = False

        return valid

    def adiciona_erro(self, message):
        errors = self._errors.setdefault(forms.forms.NON_FIELD_ERRORS, forms.utils.ErrorList())
        errors.append(message)
