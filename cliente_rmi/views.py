import Pyro5.api as Pyro5
from django.shortcuts import render, redirect, get_object_or_404
from .models import Enviar_Arquivo

# Create your views here.

URI_PYRO5 = "PYRO:obj_ae2eb3ecf13445dfa8934663a0eaaeeb@localhost:3000"

uri_server = Pyro5.Proxy(URI_PYRO5)

def home(request):
    return render(request, 'index.html')

def visualizar_arquivos(request):
    return render(request, 'visualizar.html')

def enviar_arquivos(request):
    if request.method == 'POST' and request.FILES.get('file'):
        arquivo = request.POST.get('arquivo')
        url = request.POST.get('url')

        if arquivo and url:
            try:
                Enviar_Arquivo.objects.create(nome_arquivo = arquivo, url_arquivo = url)
                return redirect('visualizar_arquivos')
            except Exception as ex:
                print(f"Erro: {ex}")
        