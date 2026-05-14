from django.db import models

# Create your models here.

class Jogo(models.Model):
    titulo = models.CharField(max_length=150)
    descricao = models.TextField()
    genero = models.CharField(max_length=100)
    plataforma = models.CharField(max_length=100)
    desenvolvedora = models.CharField(max_length=100)
    anoLancamento = models.IntegerField() 
    linkWiki = models.URLField(max_length=250, blank=True, null=True)
    linkMapa = models.URLField(max_length=250, blank=True, null=True)
    anotacoes = models.TextField(blank=True, null=True)
    capaImagem = models.ImageField(upload_to='capas_jogos/', blank=True, null=True)

    def __str__(self):
        return self.titulo