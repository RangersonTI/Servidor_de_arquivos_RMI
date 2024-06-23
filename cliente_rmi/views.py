import Pyro5.api as Pyro5
from django.shortcuts import render, redirect, get_object_or_404
from .models import Enviar_Arquivo
from django.http import Http404
from django.contrib import messages
from django.http import FileResponse
# Create your views here.

URI_PYRO5 = "PYRO:obj_64c224b013c04337a7bdabdc0270322f@localhost:3000"

uri_server = Pyro5.Proxy(URI_PYRO5)

def visualizar_arquivos(request):
    # Lógica para visualizar os arquivos
    arquivos = Enviar_Arquivo.objects.all()  # Obtém todos os arquivos salvos

    context = {
        'arquivos': arquivos,
        'title': "Visualizar arquivos"
    }
    return render(request, 'visualizar.html', context)

def enviar_arquivos(request):
    
    context = {
        'title' : "Enviar Arquivos"
    }
    
    print("Formulário enviado via POST")
    print("Conteúdo de FILES:", request.FILES)
    print("Conteúdo de POST:", request.POST)
    
    if request.method == 'POST' and request.FILES.get('file'):
        arquivo = request.FILES['file']
        nome_arquivo = request.POST.get('nome_arquivo')

        if nome_arquivo and arquivo:
            try:
                # Salvando o arquivo no banco de dados (ou fazendo outra operação necessária)
                novo_arquivo = Enviar_Arquivo(nome_arquivo=nome_arquivo, arquivo=arquivo)
                novo_arquivo.save()
                print("Arquivo salvo com sucesso")
                # Redireciona de volta para a página de visualização de arquivos
                return redirect('visualizar_arquivos')
            except Exception as ex:
                print(f"Erro ao salvar o arquivo: {ex}")

    return render(request, 'enviar.html', context)

def download_arquivo(request, nome_arquivo):
    try:
        # Localiza o arquivo na base de dados 
        # fazer 
        arquivo = Enviar_Arquivo.objects.get(nome_arquivo=nome_arquivo)
        file_path = f"uploads/{arquivo.arquivo.name}"
        return FileResponse(open(file_path, 'rb'), content_type='application/octet-stream',
                            as_attachment=True, filename=arquivo.nome_arquivo)
    except Enviar_Arquivo.DoesNotExist:
        # Se o arquivo não for encontrado, redireciona para uma página de erro ou mensagem
        return redirect('erro_page')

def deletar_arquivo(request, nome_arquivo):
    try:
        print(f"\n{nome_arquivo}\n")
        delete_arquivo = get_object_or_404(Enviar_Arquivo, nome_arquivo = nome_arquivo)
        delete_arquivo.delete()
        messages.success(request, 'Arquivo excluído com sucesso.')
        return redirect('/')
    except FileNotFoundError:
        #raise Http404(f"O arquivo '{nome_arquivo}' não foi encontrado")
        print("Arquivo não localizado")