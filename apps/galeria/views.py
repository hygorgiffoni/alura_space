'''Views do aplicativo Galeria'''
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from apps.galeria.models import Fotografia
from apps.galeria.forms import FotografiaForms

def index(request):
    '''Função para imprimir na view o código html'''
    if not request.user.is_authenticated:
        messages.error(request, 'Usuário não logado')
        return redirect('login')
    fotografias = Fotografia.objects.order_by('-data_fotografia').filter(publicada=True)
    return render(request, 'galeria/index.html', {'cards': fotografias})

def imagem(request, foto_id):
    '''Função para imprimir na view o código html'''
    fotografia = get_object_or_404(Fotografia, pk=foto_id)
    return render(request, 'galeria/imagem.html', {'fotografia': fotografia})

def buscar(request):
    '''Função para imprimir na view o código html'''
    if not request.user.is_authenticated:
        messages.error(request, 'Usuário não logado')
        return redirect('login')
    fotografias = Fotografia.objects.order_by('-data_fotografia').filter(publicada=True)

    if 'buscar' in request.GET:
        nome_buscar = request.GET['buscar']
        if nome_buscar:
            fotografias = fotografias.filter(nome__icontains=nome_buscar)

    return render(request, 'galeria/index.html', {'cards': fotografias})

def nova_imagem(request):
    '''Função para adicionar uma nova imagem na galeria'''
    if not request.user.is_authenticated:
        messages.error(request, 'Usuário não logado')
        return redirect('login')

    form = FotografiaForms()
    if request.method == 'POST':
        form = FotografiaForms(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Nova fotografia cadastrada!')
            return redirect('index')

    return render(request, 'galeria/nova_imagem.html', {'form':form})

def editar_imagem(request, foto_id):
    '''Função para editar uma nova imagem da galeria'''
    fotografia = Fotografia.objects.get(id=foto_id)
    form = FotografiaForms(instance=fotografia)

    if request.method == 'POST':
        form = FotografiaForms(request.POST, request.FILES, instance=fotografia)
        if form.is_valid():
            form.save()
            messages.success(request, 'Fotografia editada com sucesso!')
            return redirect('index')        

    return render(request, 'galeria/editar_imagem.html', {'form':form, 'foto_id':foto_id})

def deletar_imagem(request, foto_id):
    '''Função para deletar uma nova imagem da galeria'''
    fotografia = Fotografia.objects.get(id=foto_id)
    fotografia.delete()
    messages.success(request, 'A fotografia foi deletada com sucesso!')
    return redirect('index')

def filtro(request, categoria):
    '''Função para filtrar por categoria as imagens da galeria'''
    fotografias = Fotografia.objects.order_by('-data_fotografia').filter(publicada=True, categoria=categoria)

    return render(request, 'galeria/index.html', {'cards': fotografias})
