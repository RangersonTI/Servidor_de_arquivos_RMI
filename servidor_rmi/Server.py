# Caso apresente um erro ou importar o pyro5, será necessário fazer a sua instalação. 
# Para instalar, é necessário que o ambiente ´venv´ esteje ativo'. Basta executar o comando pip install Pyro5. 
# Após instalado, reiniciar o vscode e verificar se parou o erro.

import Pyro5.api as Pyro5
import Pyro5.errors as Pyro5_error

from FileService import FileService

@Pyro5.expose
class Saludo:
    def saludar(self):
        return 'Olá Mundo'

daemon = Pyro5.Daemon()

url = daemon.register(Saludo)
name_server = Pyro5.Daemon()
name_server.register('obj', url)

print(url)
daemon.requestLoop()