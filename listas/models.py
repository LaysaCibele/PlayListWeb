# listas/models.py

from django.db import models
from django.contrib.auth.models import User 
from jogos.models import Jogo             

class ListaJogos(models.Model):
    STATUS_CHOICES = [
        ('QUERO JOGAR', 'Quero Jogar'),
        ('JOGANDO', 'Jogando'),
        ('ZERADO', 'Zerado'),
    ]
    
   #Aqui eu to linkando as tabelas
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    jogo = models.ForeignKey(Jogo, on_delete=models.CASCADE)
    
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='QUERO JOGAR')
    
    def __str__(self):
        return f"{self.usuario.username} - {self.jogo.titulo} ({self.status})"