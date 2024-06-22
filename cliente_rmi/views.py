import Pyro5.api as Pyro5
from django.shortcuts import render, redirect
from .models import Enviar_Arquivo
from django.contrib import messages
from django.http import HttpResponse, JsonResponse, Http404
from django.views import View
from django.core.files.base import ContentFile
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import base64

# Create your views here.

host_porta = "192.168.1.105:3000"
uri_perso = "servidor.arquivo.rmi"
URI_PYRO5 = "PYRO:"+uri_perso+"@"+host_porta

uri_server = Pyro5.Proxy(URI_PYRO5)

@method_decorator(csrf_exempt, name="dispatch")
class Visualizar_arquivos(View):
    
    def get(self, request):
    # Lógica para visualizar os arquivos
    #arquivos = Enviar_Arquivo.objects.all()  # Obtém todos os arquivos salvos
        arquivo = uri_server.listar_arquivos()
        return JsonResponse(arquivo, safe=False)
    
        #context = {
        #    'arquivos': arquivos,
        #    'qtd_arquivos':arquivos.count,
        #    'title': "Visualizar arquivos"
        #}
        #return render(request, 'visualizar.html', context)

@method_decorator(csrf_exempt, name="dispatch")
class Enviar_arquivos(View):
    
    def post(self, request):
        if request.method == 'POST' and request.FILES.get('file'):
            nome_arquivo = request.POST['nome_arquivo']
            arquivo = request.FILES['file'].read()
            response = uri_server.enviar_arquivo(nome_arquivo, arquivo)
            return JsonResponse({'message' : response})
        
    #context = {
    #    'title' : "Enviar Arquivos"
    #}
    #
    #print("Formulário enviado via POST")
    #print("Conteúdo de FILES:", request.FILES)
    #print("Conteúdo de POST:", request.POST)
    #
    #
    #    if nome_arquivo and arquivo:
    #        try:
    #            # Salvando o arquivo no banco de dados (ou fazendo outra operação necessária)
    #            #novo_arquivo = Enviar_Arquivo(nome_arquivo=nome_arquivo, arquivo=arquivo)
    #            #novo_arquivo.save()
    #            print("Arquivo salvo com sucesso")
    #            # Redireciona de volta para a página de visualização de arquivos
    #            return redirect('visualizar_arquivos')
    #        except Exception as ex:
    #            print(f"Erro ao salvar o arquivo: {ex}")
    #
    #return render(request, 'enviar.html', context)

@method_decorator(csrf_exempt, name="dispatch")
class Download_arquivo(View):
    def get(self, request, nome_arquivo):
        arquivo = uri_server.baixar_arquivo(nome_arquivo)
        return HttpResponse(arquivo)

@method_decorator(csrf_exempt, name="dispatch")
class Deletar_arquivo(View):
    def post(self, request):
        try:
            nome_arquivo = request.POST['nome_arquivo']
            response = uri_server.excluir_arquivo(nome_arquivo)
            return JsonResponse({'message': response})
        except FileNotFoundError:
            raise Http404(f"O arquivo '{nome_arquivo}' não foi encontrado")
    #try:
    #    print(f"\n{nome_arquivo}\n")
    #    delete_arquivo = get_object_or_404(Enviar_Arquivo, nome_arquivo = nome_arquivo)
    #    delete_arquivo.delete()
    #    messages.success(request, 'Arquivo excluído com sucesso.')
    #    return redirect('/')
    #except FileNotFoundError:
    #    #raise Http404(f"O arquivo '{nome_arquivo}' não foi encontrado")
    #    print("Arquivo não localizado")