from django.contrib import admin
from .models import Clientes

class ClienteAdmin(admin.ModelAdmin):
    list_display = ['nome', 'valor', 'descricao', 'horario', 'imagem']

admin.site.register(Clientes, ClienteAdmin)