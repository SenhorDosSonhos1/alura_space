from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from galeria.models import Fotografia


def index(request):
    fotografias = Fotografia.objects.order_by("-data_fotografia").filter(publicada = True)
    return render(request, 'galeria/index.html', context = {"fotografias": fotografias})

def imagem(request, id):
    fotografia = get_object_or_404(Fotografia, id = id)
    return render(request, 'galeria/imagem.html', context = {"fotografia": fotografia})