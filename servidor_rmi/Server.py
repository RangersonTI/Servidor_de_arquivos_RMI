# Caso apresente um erro ou importar o pyro5, será necessário fazer a sua instalação. 
# Para instalar, é necessário que o ambiente ´venv´ esteje ativo'. Basta executar o comando pip install Pyro5. 
# Após instalado, reiniciar o vscode e verificar se parou o erro.

from tkinter import *
from tkinter.ttk import Label
import Pyro5.api as Pyro5
import platform, os, socket
from FileService import FileService

porta = 3000

class Server:
    def main():
        diretorio = verificar_SO()
        file_service = FileService(diretorio)

        daemon = Pyro5.Daemon(port=porta,host=str(meu_ip()))
        uri = daemon.register(file_service, 'servidor.arquivo.rmi')
        print(f"Serviço de arquivo em funcionamento. \nURI: {uri}")

        daemon.requestLoop()


def iniciar_servidor():

    if __name__ == "__main__":
        Server.main()

    print("Servidor Iniciado")

def fechar_servidor():
    exit()

def verificar_SO():
    so_atual = platform.system()

    if so_atual == "Linux":
        usuario = os.getlogin()
        return f"/home/{usuario}/media"
    elif so_atual == "Windows":
        return "C:\\media"
    
def meu_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
    finally:
        s.close()
    return ip


############################## INTERFACE GRÁFICA ##############################

#### CRIAÇÃO DA JANELA ####
window = Tk()
window.title("Servidor")
window.geometry("600x400")
window.configure(background="#91c29b")


#### CRIAÇÃO DA LOGO ####
logo = PhotoImage(file="servidor_rmi/assets/server_file.png", width=160, height=160)

label_logo = Label(window, image=logo, justify="center", background="#91c29b")
window.update()
label_logo.place(x=(window.winfo_width()/2 - 75),y=20,width=150, height=150)


#### CRIAÇÃO DA LABEL E TEXTBOX PARA CADASTRO DA ''PORTA'' ####
label_porta = Label(window, text=f"Porta: {porta}", font=("Arial","14","bold"), justify="center", background="#91c29b")
label_porta.place(x=(window.winfo_width()/2 - 50), y=window.winfo_height()/2 + 30, width=110, height=25)


#### CRIAÇÃO DE UM BOTÃO PARA FAZER A ENTRADA DA PORTA OU CANCELAR ####
botao_iniciar = Button(window, text="Iniciar", font=("Velvica","16","bold"), justify="center", background="#31693c", foreground="#ededed", command=iniciar_servidor)
botao_iniciar.place(x=(window.winfo_width()/2 - botao_iniciar.winfo_width()) - 160, y=window.winfo_height()/2 + 130, width=140, height=30)

botao_cancelar = Button(window, text="Cancelar", font=("Velvica","16","bold"), justify="center", background="#d13f3f", foreground="#ededed", command=fechar_servidor)
botao_cancelar.place(x=(window.winfo_width()/2 - botao_cancelar.winfo_width()) + 40, y=window.winfo_height()/2 + 130, width=140, height=30)
window.mainloop()