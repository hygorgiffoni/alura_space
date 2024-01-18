from django.shortcuts import render

def index(request):
    '''Função para imprimir na view o código html'''
    return render(request, 'galeria/index.html')

def imagem(request):
    '''Função para imprimir na view o código html'''
    return render(request, 'galeria/imagem.html')
