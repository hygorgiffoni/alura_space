from datetime import datetime
from django.db import models
from django.contrib.auth.models import User


class Fotografia(models.Model):
    '''Tabela dos dados relacionados a fotografias'''
    CATEGORIAS = [
        ('NEBULOSA', 'Nebulosa'),
        ('ESTRELA', 'Estrela'),
        ('GALÁXIA', 'Galáxia'),
        ('PLANETA', 'Planeta')
    ]

    nome = models.CharField(max_length=100, null=False, blank=False)
    legenda = models.CharField(max_length=150, null=False, blank=False)
    categoria = models.CharField(max_length=100, choices=CATEGORIAS, default='')
    descricao = models.TextField(null=False, blank=False)
    foto = models.ImageField(upload_to='fotos/%Y/%m/%d', blank=True)
    publicada = models.BooleanField(default=True)
    data_fotografia = models.DateTimeField(default=datetime.now, blank=False)
    usuario = models.ForeignKey(
        to=User,
        on_delete=models.SET_NULL,
        null=True,
        blank=False,
        related_name='user',
    )

    def __str__(self):
        '''Retorna o nome do modelo'''
        return self.nome
