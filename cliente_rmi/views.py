from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'index.html')

def visualizar_arquivos(request):
    return render(request, 'visualizar.html')

def enviar_arquivos(request):
    return render(request, 'enviar.html')