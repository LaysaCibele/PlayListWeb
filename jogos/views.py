from django.shortcuts import render, get_object_or_404
from .models import Jogo

# Create your views here.

def pagina_do_jogo(request, id_do_jogo):
    jogo_encontrado = get_object_or_404(Jogo, id=id_do_jogo)
    
    return render(request, 'jogo.html', {'jogo': jogo_encontrado})
