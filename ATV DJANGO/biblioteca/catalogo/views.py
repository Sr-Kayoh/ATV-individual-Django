from django.shortcuts import render, redirect, get_object_or_404
from .models import Autor, Livro
from .forms import AutorForm, LivroForm

def autor_list(request):
    autores = Autor.objects.all()
    return render(request, 'catalogo/autor_list.html', {'autores': autores})

def autor_create(request):
    if request.method == "POST":
        form = AutorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('autor_list')
    else:
        form = AutorForm()
    return render(request, 'catalogo/autor_form.html', {'form': form})

def autor_update(request, pk):
    autor = get_object_or_404(Autor, pk=pk)
    if request.method == "POST":
        form = AutorForm(request.POST, instance=autor)
        if form.is_valid():
            form.save()
            return redirect('autor_list')
    else:
        form = AutorForm(instance=autor)
    return render(request, 'catalogo/autor_form.html', {'form': form})

def autor_delete(request, pk):
    autor = get_object_or_404(Autor, pk=pk)
    if request.method == "POST":
        autor.delete()
        return redirect('autor_list')
    return render(request, 'catalogo/autor_confirm_delete.html', {'autor': autor})

def livro_list(request):
    livros = Livro.objects.all()
    return render(request, 'catalogo/livro_list.html', {'livros': livros})

def livro_create(request):
    if request.method == "POST":
        form = LivroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('livro_list')
    else:
        form = LivroForm()
    return render(request, 'catalogo/livro_form.html', {'form': form})

def livro_update(request, pk):
    livro = get_object_or_404(Livro, pk=pk)
    if request.method == "POST":
        form = LivroForm(request.POST, instance=livro)
        if form.is_valid():
            form.save()
            return redirect('livro_list')
    else:
        form = LivroForm(instance=livro)
    return render(request, 'catalogo/livro_form.html', {'form': form})

def livro_delete(request, pk):
    livro = get_object_or_404(Livro, pk=pk)
   