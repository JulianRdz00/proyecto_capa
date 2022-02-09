from cursos.models import Curso, Modulos, Video
from .forms import CursoForm
from .forms import ModulosForm
from .forms import VideoForm
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


def nuevo_modulo(request):
    if request.method == "POST":
        form = ModulosForm(request.POST)
        if form.is_valid():
            modulos = form.save()
            return redirect('detalle_modulo', pk=modulos.pk)
    else:
        form = ModulosForm()
    return render(request, 'cursos/nuevo_modulo.html', {'form': form})


def nuevo_video(request):
    if request.method == "POST":
        form = VideoForm(request.POST)
        if form.is_valid():
            video = form.save()
            return redirect('detalle_video', pk=video.pk)
    else:
        form = VideoForm()
    return render(request, 'cursos/nuevo_video.html', {'form': form})


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


def detalle_video(request, pk):
    video = get_object_or_404(Video, pk=pk)
    return render(request, 'cursos/detalle_video.html', {'video': video})


def editar_video(request, pk):
    video = get_object_or_404(Video, pk=pk)
    if request.method == "POST":
        form = VideoForm(request.POST, instance=video)
        if form.is_valid():
            video = form.save()
            return redirect('detalle_video', pk=video.pk)
    else:
        form = VideoForm(instance=video)
    return render(request, 'cursos/nuevo_video.html', {'form': form})
    