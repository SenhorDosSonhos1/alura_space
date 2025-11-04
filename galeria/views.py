from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from galeria.models import Fotografia


def index(request):
    fotografias = Fotografia.objects.order_by("-data_fotografia").filter(publicada = True)
    return render(request, 'galeria/index.html', context = {"fotografias": fotografias})

def imagem(request, id):
    fotografia = get_object_or_404(Fotografia, id = id)
    return render(request, 'galeria/imagem.html', context = {"fotografia": fotografia})

def buscar(request):
    fotografias = Fotografia.objects.order_by("-data_fotografia").filter(publicada = True)

    if "buscar" in request.GET:
        nome_a_buscar = request.GET['buscar']
        if nome_a_buscar:
            fotografias = fotografias.filter(nome__icontains=nome_a_buscar)

    return render(request, 'galeria/buscar.html', {'fotografias': fotografias})