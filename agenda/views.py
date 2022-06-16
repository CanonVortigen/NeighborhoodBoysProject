from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Clientes
from .forms import ClientesForm


#Metodo responsavel por VISUALIZAR os Clientes
@login_required
def HomePage(request):
    buscar_clientes = Clientes.objects.all()
    return render(request, 'home_page.html', {'clientes': buscar_clientes})


#Metodo responsavel por fazer o CREATE do Cliente
@login_required
def CadastarCliente(request):
    form = ClientesForm(request.POST or None, request.FILES or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('homepage')
    return render(request, 'novo_cliente.html', {'form': form})

#Metodo responsavel por fazer um UPDATE do Cliente
@login_required
def EditarCliente(request, pk):
    buscar_clientes = get_object_or_404(Clientes, pk=pk)
    form = ClientesForm(request.POST or None, request.FILES or None, instance=buscar_clientes)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('homepage')
    return render(request, 'editar_cliente.html', {'form': form})

#Metodo responsavel por fazer o VISUALIZAR os detalhes do Cliente
@login_required
def DetalhesCliente(request, pk):
    buscar_clientes = get_object_or_404(Clientes, pk=pk)
    return render(request, 'detalhes_cliente.html', {'detalhes': buscar_clientes})

#Metodo responsavel por fazer o DELETE do Cliente
@login_required
def DeletarCliente(request, pk):
    buscar_clientes = get_object_or_404(Clientes, pk=pk)
    #form = ClientesForm(request.POST or None, request.FILES or None, instance=buscar_clientes)
    if request.method == 'POST':
        buscar_clientes.delete()
        return redirect('homepage')

    return render(request, 'deletar_cliente.html', {'deletar': buscar_clientes})