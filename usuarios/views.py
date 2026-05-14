from django.shortcuts import render, redirect
from django.contrib.auth.forms import User
from django.contrib.auth import login
from django.contrib import messages


def cadastro_page(request):
    if request.method == 'POST':
        nome_usuario = request.POST.get('username')
        email_usuario = request.POST.get('email')
        senha_usuario = request.POST.get('password')
        
        if User.objects.filter(username=nome_usuario).exists():
            messages.error(request, "Este nome de usuário já está em uso.")
            return render(request, 'cadastro.html')
            
        user = User.objects.create_user(
            username=nome_usuario,
            email=email_usuario,
            password=senha_usuario
        )
        login(request, user) 
        
        return redirect('catalogo')
    
    
    return render(request, 'cadastro.html')


def catalogo_page(request):
    return render(request, 'catalogo.html')
