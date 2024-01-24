from django.shortcuts import render, get_object_or_404
from galeria.models import Fotografia

def index(request):
    '''Função para imprimir na view o código html'''
    fotografias = Fotografia.objects.order_by('-data_fotografia').filter(publicada=True)
    return render(request, 'galeria/index.html', {'cards': fotografias})

def imagem(request, foto_id):
    '''Função para imprimir na view o código html'''
    fotografia = get_object_or_404(Fotografia, pk=foto_id)
    return render(request, 'galeria/imagem.html', {'fotografia': fotografia})

def buscar(request):
    '''Função para imprimir na view o código html'''
    fotografias = Fotografia.objects.order_by('-data_fotografia').filter(publicada=True)

    if 'buscar' in request.GET:
        nome_buscar = request.GET['buscar']
        if nome_buscar:
            fotografias = fotografias.filter(nome__icontains=nome_buscar)

    return render(request, 'galeria/buscar.html', {'cards': fotografias})