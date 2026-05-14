from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class ListaJogos(models.Model):
    STATUS_CHOICE = [
        ('QUERO JOGAR', 'Quero_Jogar'),
        ('JOGANDO', 'Jogando'),
        ('ZERADO', 'Zerado'),
    ]
    
