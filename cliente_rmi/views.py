import Pyro5.api as Pyro5
from django.shortcuts import render, redirect, get_object_or_404
from .models import Enviar_Arquivo

# Create your views here.

URI_PYRO5 = "PYRO:obj_ae2eb3ecf13445dfa8934663a0eaaeeb@localhost:3000"

uri_server = Pyro5.Proxy(URI_PYRO5)

def visualizar_arquivos(request):
    # Lógica para visualizar os arquivos
    arquivos = Enviar_Arquivo.objects.all()  # Obtém todos os arquivos salvos

    context = {
        'arquivos': arquivos
    }
    return render(request, 'visualizar.html', context)

def enviar_arquivos(request):
    if request.method == 'POST' and request.FILES.get('file'):
        arquivo = request.FILES['file']
        nome_arquivo = request.POST.get('nome_arquivo', '')
        url_arquivo = request.POST.get('url_arquivo', '')

        if nome_arquivo and url_arquivo:
            try:
                # Salvando o arquivo no banco de dados (ou fazendo outra operação necessária)
                novo_arquivo = Enviar_Arquivo(nome_arquivo=nome_arquivo, url_arquivo=url_arquivo, arquivo=arquivo)
                novo_arquivo.save()

                # Redireciona de volta para a página de visualização de arquivos
                return redirect('visualizar_arquivos')
            except Exception as ex:
                print(f"Erro ao salvar o arquivo: {ex}")

    return render(request, 'enviar.html')