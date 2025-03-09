from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from .models import Marca
from .forms import MarcaForm
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth.decorators import login_required
@login_required
def gestionar_marcas(request, id=None):
    query = request.GET.get('buscar', '')
    marcas_list = Marca.objects.filter(nombre__icontains=query) if query else Marca.objects.all()

    paginator = Paginator(marcas_list, 2)
    page_number = request.GET.get('page')
    marcas = paginator.get_page(page_number)

    if request.method == 'POST':
        if id:
            marca = get_object_or_404(Marca, id=id)
            form = MarcaForm(request.POST, instance=marca)
            mensaje = "Marca actualizada con éxito"
        else:
            form = MarcaForm(request.POST)
            mensaje = "Marca creada con éxito"

        if form.is_valid():
            form.save()
            messages.success(request, mensaje) 
            return redirect('Gestionar Marcas')
    else:
        if id:
            marca = get_object_or_404(Marca, id=id)
            form = MarcaForm(instance=marca)
        else:
            form = MarcaForm()

    return render(request, 'Marcas/marcas_list.html', {
        'marcas': marcas,
        'form': form,
    })
