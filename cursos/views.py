from genericpath import exists
from operator import ge
from cursos.models import Categoria, Curso, Modulos
from .forms import CategoriaForm
from .forms import CursoForm
from .forms import ModulosForm
from django.shortcuts import redirect
from django.shortcuts import render, get_object_or_404


def nuevo_curso(request):
    if request.method == "POST":
        form = CursoForm(request.POST)
        if form.is_valid():
            curso = form.save(commit=False)
            curso.autor = request.user
            curso.save()
            return redirect('detalle_curso', pk=curso.pk)
    else:
        form = CursoForm()
    return render(request, 'cursos/nuevo_curso.html', {'form': form})


def detalle_curso(request, pk):
    curso = get_object_or_404(Curso, pk=pk)
    return render(request, 'cursos/detalle_curso.html', {'curso': curso})


def editar_curso(request, pk):
    curso = get_object_or_404(Curso, pk=pk)
    if request.method == "POST":
        form = CursoForm(request.POST, instance=curso)
        if form.is_valid():
            curso = form.save(commit=False)
            curso.autor = request.user
            curso.save()
            return redirect('detalle_curso', pk=curso.pk)
    else:
        form = CursoForm(instance=curso)
    return render(request, 'cursos/nuevo_curso.html', {'form': form})


def nuevo_modulo(request):
    if request.method == "POST":
        form = ModulosForm(request.POST)
        if form.is_valid():
            modulos = form.save()
            return redirect('detalle_modulo', pk=modulos.pk)
    else:
        form = ModulosForm()
    return render(request, 'cursos/nuevo_modulo.html', {'form': form})


def detalle_modulo(request, pk):
    modulo = get_object_or_404(Modulos, pk=pk)
    return render(request, 'cursos/detalle_modulo.html', {'modulo': modulo})


def editar_modulo(request, pk):
    modulo = get_object_or_404(Modulos, pk=pk)
    if request.method == "POST":
        form = ModulosForm(request.POST, instance=modulo)
        if form.is_valid():
            modulo = form.save()
            return redirect('detalle_modulo', pk=modulo.pk)
    else:
        form = ModulosForm(instance=modulo)
    return render(request, 'cursos/nuevo_modulo.html', {'form': form})


def nueva_categoria(request):
    if request.method == "POST":
        form = CategoriaForm(request.POST)
        if form.is_valid():
            categoria = form.save()
            return redirect('detalle_categoria', pk=categoria.pk)
    else:
        form = CategoriaForm()
    return render(request, 'cursos/nueva_categoria.html', {'form': form})


def detalle_categoria(request, pk):
    categoria = get_object_or_404(Categoria, pk=pk)
    return render(request, 'cursos/detalle_categoria.html', {'categoria': categoria})


def editar_categoria(request, pk):
    categoria = get_object_or_404(Categoria, pk=pk)
    if request.method == 'POST':
        form = CategoriaForm(request.POST, instance=categoria)
        if form.is_valid():
            categoria = form.save()
            return redirect('detalle_categoria', pk=categoria.pk)
    else:
        form = CategoriaForm(instance=categoria)
    return render(request, 'cursos/nueva_categoria.html', {'form': form})


def curso_video(request, pk, pk_modulo):
    curso = get_object_or_404(Curso, pk=pk)
    modulo = get_object_or_404(Modulos, pk=pk_modulo)
    return render(request, 'cursos/modulo_video.html', {'curso': curso, 'modulo': modulo})


def curso_descripcion(request, pk, pk_modulo, pk_categoria):
    curso = get_object_or_404(Curso, pk=pk)
    modulo = get_object_or_404(Modulos, pk=pk_modulo)
    categoria = get_object_or_404(Categoria, pk=pk_categoria)
    return render(request, 'cursos/descripcion.html', {'curso': curso, 'modulo': modulo, 'categoria': categoria})


def curso_showtime(request, pk, pk_modulo, pk_categoria):
    curso = get_object_or_404(Curso, pk=pk)
    modulo = get_object_or_404(Modulos, pk=pk_modulo)
    categoria = get_object_or_404(Categoria, pk=pk_categoria)
    return render(request, 'cursos/modulo_vista.html', {'curso': curso, 'modulo': modulo, 'categoria': categoria})
