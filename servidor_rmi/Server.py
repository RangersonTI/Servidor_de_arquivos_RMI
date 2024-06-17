# Caso apresente um erro ou importar o pyro5, será necessário fazer a sua instalação. 
# Para instalar, é necessário que o ambiente ´venv´ esteje ativo'. Basta executar o comando pip install Pyro5. 
# Após instalado, reiniciar o vscode e verificar se parou o erro.

import Pyro5.api
from FileService import FileService

def main():
    # Cria o objeto de serviço de arquivo
    file_service = FileService()

    # Inicia o daemon Pyro
    daemon = Pyro5.api.Daemon()

    # Registra o objeto de serviço no daemon
    uri = daemon.register(file_service)

    # Disponibiliza o serviço para o nome "FileService"
    ns = Pyro5.api.locate_ns(host="nameserver", port=3000)
    ns.register("serverrmi", uri)

    print("FileService is running. URI:", uri)

    # Mantém o servidor rodando
    daemon.requestLoop()

if __name__ == "__main__":
    main()