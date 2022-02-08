import datetime
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from .forms import Perfiles
from .forms import FormPerfiles
from django.shortcuts import redirect


def perfil_list(request):
    lista_perfiles = Perfiles.objects.order_by('profesion')
    return render(request, 'perfiles/perfil_list.html', {'lista_perfiles': lista_perfiles})

def perfil_detail(request, pk):
    post = get_object_or_404(Perfiles, pk=pk)
    return render(request, 'perfiles/perfil_detail.html', {'post': post})

def perfil_new(request):
    if request.method == "POST":
        form = FormPerfiles(request.POST)
        if form.is_valid():
            edit = form.save(commit=False)
            edit.user = request.user
            edit.published_date = timezone.now()
            edit.save()
            return redirect('perfil_detail', pk=edit.pk)
    else:
        form = FormPerfiles()        
    return render(request, 'perfiles/perfil_new.html', {'form': form})

def perfil_edit(request,pk):
    post = get_object_or_404(Perfiles, pk=pk)
    if request.method == "POST":
        form = FormPerfiles(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('perfil_detail', pk=post.pk)
    else:
        form = FormPerfiles(instance=post)
    return render(request, 'perfiles/perfil_new.html', {'form': form})