import sys
import Pyro5.api as Pyro5
from cliente_rmi.models import Enviar_Arquivo

@Pyro5.expose
class FileService():
    
    def __init__(self, uri):
        self.diretorio = uri

    def listar_arquivos(self):
        try:
            arquivos = Enviar_Arquivo.objects.all()
            return [arquivo.nome_arquivo for arquivo in arquivos]
        except Exception as ex:
            return str(f"Erro: {ex}")

    def baixar_arquivo(self, nome_arquivo):
        # Implementar lógica para baixar o arquivo
        return "Função baixar_arquivo não implementada"

    def enviar_arquivo(self, nome_arquivo, arquivo):
        try:
            novo_arquivo = Enviar_Arquivo(nome_arquivo=nome_arquivo, arquivo=arquivo)
            novo_arquivo.save()
            return "Arquivo enviado com sucesso"
        except Exception as ex:
            return str(f"Erro: {ex}")

    def excluir_arquivo(self, nome_arquivo):
        try:
            delete_arquivo = Enviar_Arquivo.objects.get(nome_arquivo=nome_arquivo)
            delete_arquivo.delete()
            return "Arquivo deletado com sucesso"
        except Exception as ex:
            return str(f"Erro: {ex}")