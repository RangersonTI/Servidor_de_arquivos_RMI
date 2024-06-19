# árvore do projeto
```html
<div style="background-color: black; padding: 100px; width: 50%; margin: 0 auto; text-align: center;">
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
│   ├── templates/<br>
│   │   ├── base/<br>
│   │   │   ├── base.html<br>
│   │   │   └── menu.html<br>
│   │   ├── static/<br>
│   │   │   └── css/<br>
│   │   │       └── style.css<br>
│   │   ├── enviar.html<br>
│   │   └── visualizar.html<br>
│<br>
├── <b>media/</b><br>
│   ├── uploads/<br>
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
``````


# MODIFICAÇÕES ALISSON

- settings.py do servidor_de_arquivos_rmi
- models.py do cliente_rmi
- urls.py do servidor_de_arquivos_rmi

<b>o banco de dados já foi construído</b>





# requisitos 

- <b>(1)LOGIN</b> Os clientes deverão se conectar ao servidor com as informações necessárias;
- <b>(2)VISUALIZAR</b> Os clientes poderão visualizar os arquivos presentes no servidor após a conexão;
- <b>(3)FUNÇÃO ENVIAR</b> Os clientes poderão enviar os arquivos a partir da interface para o servidor que deverá disponibilizar
aos demais clientes conectados;
- <b>(4)FUNÇÃO DELETE</b> Os clientes poderão excluir os arquivos presentes no servidor, independentemente de quem tenha feito
o upload;
- <b>(5)FUNÇÃO GET ARQUIVO</b> Os clientes poderão efetuar o download dos arquivos presentes no servidor.

# funções 

- camada view (FUNÇÕES NECESSÁRIAS PARA O FUNCIONAMENTO DA APLICAÇÃO)

- camada model (ENVIAR E DELETE)

- camada template (VISUALIZAR OS ARQUIVOS) e (LOGIN)


# contribuintes

- <b>RANGERSON</b> interface do servidor
- <b>ALISSON</b> -> camada model
- <b>LUIS FELIPE</b> view
- <b>ISRAEL</b> -> login

# Dependências
Pyro5 -> pip install Pyro5
Tkinter -> sudo apt-get install python3-tk (Linux)
Django -> pip install django
