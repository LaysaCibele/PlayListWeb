from django.shortcuts import render

def biblioteca_view(request):
    return render(request, 'biblioteca.html')