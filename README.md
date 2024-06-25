# ARVORE DO PROJETO

<div>
<b>Servidor_de_arquivos_RMI/</b> <br>
│<br>
├── <b>cliente_rmi/</b><br>
│   ├── __init__.py<br>
│   ├── admin.py<br>
│   ├── apps.py<br>
│   ├── migrations/<br>
│   │   ├── __init__.py<br>
│   │   └── __pycache__/<br>
│   │       ├── __init__.cpython-311.pyc<br>
│   │       └── __init__.cpython-312.pyc<br>
│   ├── models.py<br>
│   ├── tests.py<br>
│   ├── views.py<br>
│   ├── static<br>
│   │   ├── css/<br>
│   │   │   └── style.css<br>
│   │   └── img/<br>
│   │       ├── download.png<br>
│   │       ├── excluir.png<br>
│   │       ├── fundologin.jpg<br>
│   │       └── server_file.ico<br>
│   ├── templates/<br>
│   │   ├── base/<br>
│   │   │   ├── base.html<br>
│   │   │   ├── footer.html<br>
│   │   │   └── menu.html<br>
│   │   ├── enviar.html<br>
│   │   ├── login.html<br>
│   │   └── visualizar.html<br>
│<br>
├── <b>media/</b><br>
│       └── uploads/<br>
|<br>
├── <b>servidor_de_arquivos_rmi/</b><br>
│   ├── __init__.py<br>
│   ├── asgi.py<br>
│   ├── settings.py<br>
│   ├── urls.py<br>
│   ├── wsgi.py<br>
│   └── __pycache__/<br>
│       ├── __init__.cpython-311.pyc<br>
│       └── __init__.cpython-312.pyc<br>
│<br>
├── <b>servidor_rmi/</b><br>                                                                       
│   ├── __init__.py<br>
│   ├── assets/<br>
│   │   └── server_file.png<br>
│   ├── Client.py<br>
│   ├── FileService.py<br>
│   ├── Server.py<br>
│   └── __pycache__/<br>
│       ├── Client.cpython-311.pyc<br>
│       ├── FileService.cpython-311.pyc<br>
│       └── Server.cpython-311.pyc<br>
│<br>
├── db.sqlite3<br>
├── manage.py<br>
├── README.md<br>
└── .gitignore<br>
</div>


# REQUISITOS 

- <b>(1)LOGIN</b> Os clientes deverão se conectar ao servidor com as informações necessárias;
- <b>(2)VISUALIZAR</b> Os clientes poderão visualizar os arquivos presentes no servidor após a conexão;
- <b>(3)FUNÇÃO ENVIAR</b> Os clientes poderão enviar os arquivos a partir da interface para o servidor que deverá disponibilizar
aos demais clientes conectados;
- <b>(4)FUNÇÃO DELETE</b> Os clientes poderão excluir os arquivos presentes no servidor, independentemente de quem tenha feito
o upload;
- <b>(5)FUNÇÃO GET ARQUIVO</b> Os clientes poderão efetuar o download dos arquivos presentes no servidor.

# FUNÇÕES 

- camada view (FUNÇÕES NECESSÁRIAS PARA O FUNCIONAMENTO DA APLICAÇÃO)

- camada model (ENVIAR E DELETAR)

- camada template (VISUALIZAR OS ARQUIVOS) e (LOGIN) - FRONT END


# CONTRIBUINTES

- <b>RANGERSON</b> SERVIDOR / FUNÇÃO ENVIAR / DELETAR
- <b>ALISSON</b> -> BANCO DE DADOS
- <b>LUIS FELIPE</b> FUNÇÃO VISUALIZAR / BAIXAR
- <b>ISRAEL</b> -> LOGIN

# DEPENDÊNCIAS
<br>Pyro5 -> pip install Pyro5
<br>Tkinter -> sudo apt-get install python3-tk (Linux)
<br>Django -> pip install django

# FUNCIONAMENTO
<br><b>1. Funcionamento do servidor RMI: </b>Primeiramente, deve-se executar a interface servidor RMI, com o arquivo <a href="#">Server.py</a>, da pasta <i>servidor_rmi</i>. Será carregado a interface gráfica, e para iniciar o servidor, clique em 'Iniciar'.
<p>Será gerado um token e mostrado no <b>console</b>. Esse token será utilizado na interface do cliente para realização do login<p>

<br><b>2. Execução da aplicação (Django): </b> Após a execução do servidor RMI, proximo passo é a execução do django para iniciar a aplicação.

<br><b>3. Login: </b> Feito a execução do django, faça o login utilizando o token fornecido pelo <b>servidor RMI</b> e aproveite😎
