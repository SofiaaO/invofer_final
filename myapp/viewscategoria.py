from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from .models import Categoria
from .forms import CategoriaForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
@login_required
def gestionar_categorias(request, id=None):
    query = request.GET.get('buscar', '')
    categorias_list = Categoria.objects.filter(nombre__icontains=query) if query else Categoria.objects.all()
    paginator = Paginator(categorias_list, 5)
    page_number = request.GET.get('page')
    categorias = paginator.get_page(page_number)

    if request.method == 'POST':
        if id:
            categoria = get_object_or_404(Categoria, id=id)
            form = CategoriaForm(request.POST, instance=categoria)
            mensaje = "Categoria actualizada con éxito"
        else:
            form = CategoriaForm(request.POST)
            mensaje = "Categoria creada con éxito"
        if form.is_valid():
            form.save()
            messages.success(request, mensaje) 
            return redirect('Gestionar Categorias')
    else:
        if id:
            categoria = get_object_or_404(Categoria, id=id)
            form = CategoriaForm(instance=categoria)
        else:
            form = CategoriaForm()

    return render(request, 'Categorias/categorias_list.html', {
        'categorias': categorias,
        'form': form,
    })