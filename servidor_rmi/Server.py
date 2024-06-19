# Caso apresente um erro ou importar o pyro5, será necessário fazer a sua instalação. 
# Para instalar, é necessário que o ambiente ´venv´ esteje ativo'. Basta executar o comando pip install Pyro5. 
# Após instalado, reiniciar o vscode e verificar se parou o erro.

from tkinter import *
from tkinter.ttk import Label
import platform
import Pyro5.api as Pyro5
from FileService import FileService

class Server:
    def main():
        file_service = FileService()
        daemon = Pyro5.Daemon(port=3000)
        uri = daemon.register(file_service)
        
        name_server = Pyro5.locate_ns()
        name_server.register("obj", uri)
        
        print(f"Serviço de arquivo em funcionamento. \nURI: {uri}")
        daemon.requestLoop()
        
    

    
def iniciar_servidor():
    
    if __name__ == "__main__":
        Server.main()
        
    print("Servidor Iniciado")

def fechar_servidor():

    global server_process
    if server_process:
        server_process.kill()
        server_process = None
        exit()
    else:
        exit()
        

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
label_porta = Label(window, text="Porta:", font=("Arial","14","bold"), justify="center", background="#91c29b")
label_porta.place(x=(window.winfo_width()/2 - 90), y=window.winfo_height()/2 + 30, width=60, height=25)
 
textBox_porta = Text(window, font=("Arial","12"))
textBox_porta.place(x=(window.winfo_width()/2 - 25), y=window.winfo_height()/2 + 30,width= 120, height=25)


#### CRIAÇÃO DE UM BOTÃO PARA FAZER A ENTRADA DA PORTA OU CANCELAR ####
botao_iniciar = Button(window, text="Iniciar", font=("Velvica","16","bold"), justify="center", background="#31693c", foreground="#ededed", command=iniciar_servidor)
botao_iniciar.place(x=(window.winfo_width()/2 - botao_iniciar.winfo_width()) - 160, y=window.winfo_height()/2 + 130, width=140, height=30)

botao_cancelar = Button(window, text="Cancelar", font=("Velvica","16","bold"), justify="center", background="#d13f3f", foreground="#ededed", command=fechar_servidor)
botao_cancelar.place(x=(window.winfo_width()/2 - botao_cancelar.winfo_width()) + 40, y=window.winfo_height()/2 + 130, width=140, height=30)
window.mainloop()