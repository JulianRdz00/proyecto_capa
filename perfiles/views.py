import datetime
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from .forms import Perfiles
from .forms import FormPerfiles
from django.shortcuts import redirect


def perfil_lista(request):
    lista_perfiles = Perfiles.objects.order_by('profesion')
    return render(request, 'perfiles/perfil_lista.html', {'lista_perfiles': lista_perfiles})


def perfil_detalle(request, pk):
    perfil_detalle = get_object_or_404(Perfiles, pk=pk)
    return render(request, 'perfiles/perfil_detalle.html', {'perfil_detalle': perfil_detalle})


def perfil_nuevo(request):
    if request.method == "POST":
        form = FormPerfiles(request.POST)
        if form.is_valid():
            nuevo = form.save(commit=False)
            nuevo.user = request.user
            nuevo.save()
            return redirect('perfil_detalle', pk=nuevo.pk)
    else:
        form = FormPerfiles()
    return render(request, 'perfiles/perfil_nuevo.html', {'form': form})


def perfil_editar(request,pk):
    editar = get_object_or_404(Perfiles, pk=pk)
    if request.method == "POST":
        form = FormPerfiles(request.POST, instance=editar)
        if form.is_valid():
            editar = form.save(commit=False)
            editar.user = request.user
            editar.save()
            return redirect('perfil_detalle', pk=editar.pk)
    else:
        form = FormPerfiles(instance=editar)
    return render(request, 'perfiles/perfil_nuevo.html', {'form': form})
