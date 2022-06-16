from django import forms
from .models import Clientes

class ClientesForm(forms.ModelForm):
    class Meta:
        model = Clientes
        fields = ['nome', 'valor', 'descricao', 'horario', 'imagem']
        widgets = {
            'nome': forms.TextInput(attrs={'placeholder':'Nome', 'class': 'form-control form-control-lg'}),
            'apelido': forms.TextInput(attrs={'placeholder':'Apelido', 'class': 'form-control form-control-lg'}),
            'descricao': forms.Textarea(attrs={'placeholder':'Descricao', 'class': 'form-control form-control-lg'}),
            'valor': forms.TextInput(attrs={'placeholder':'Valor', 'class': 'form-control form-control-lg'}),
            'horario': forms.TextInput(attrs={'placeholder':'Horario', 'class': 'form-control form-control-lg','autocomplete':'off'}),
            'imagem': forms.FileInput(attrs={'id':'validatedCustomFile'})
        }