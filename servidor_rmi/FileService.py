import os
import Pyro5.api as Pyro5

@Pyro5.expose
class FileService:

    def __init__(self, diretorio):
        self.diretorio = diretorio

        if not os.path.exists(diretorio):
            os.makedirs(diretorio)

    def listar_arquivos(self):
        try:
            return os.listdir(self.diretorio)
        except Exception as ex:
            return str(f"Erro: {ex}")

    def baixar_arquivo(self, nome_arquivo):
        try:
            arquivo = os.path.join(self.diretorio, nome_arquivo)
            with open(arquivo, 'rb') as arquivo_down:
                return arquivo_down.read()
        except Exception as ex:
            return str(f"Erro: {ex}")

    def enviar_arquivo(self, nome_arquivo, data):
        try:
            arquivo = os.path.join(self.diretorio, nome_arquivo)
            with open(arquivo,'wb') as arquivo_up:
                arquivo_up.write(data)
                print(f"Arquivo ´{nome_arquivo}´ enviado")
        except Exception as ex:
            return str(f"Erro: {ex}")

    def excluir_arquivo(self, nome_arquivo):
        arquivo = os.path.join(self.diretorio, nome_arquivo)

        if os.path.exists(arquivo):
            os.remove(arquivo)