from django import forms

from .models import Cliente

class ClienteForm(forms.ModelForm):

    class Meta:
        model = Cliente
        fields = ('nome', 'sexo' , 'data', 'peso' , 'altura', 'imc', 'avaliacao', 'endereco', 'telefone', 'plano', 'meta','ativo', 'photo', 'user', 'id')