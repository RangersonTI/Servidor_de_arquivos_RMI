# árvore do projeto

Servidor_de_arquivos_RMI/
│
├── cliente_rmi/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations/
│   │   ├── __init__.py
│   │   └── __pycache__/
│   │       ├── __init__.cpython-311.pyc
│   │       └── __init__.cpython-312.pyc
│   ├── models.py
│   ├── tests.py
│   ├── views.py
│   ├── templates/
│   │   ├── base/
│   │   │   ├── base.html
│   │   │   └── menu.html
│   │   ├── static/
│   │   │   └── css/
│   │   │       └── style.css
│   │   ├── enviar.html
│   │   └── visualizar.html
│
├── media/
│   ├── uploads/
|
├── servidor_de_arquivos_rmi/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── __pycache__/
│       ├── __init__.cpython-311.pyc
│       └── __init__.cpython-312.pyc
│
├── servidor_rmi/
│   ├── __init__.py
│   ├── assets/
│   │   └── server_file.png
│   ├── Client.py
│   ├── FileService.py
│   ├── Server.py
│   └── __pycache__/
│       ├── Client.cpython-311.pyc
│       ├── FileService.cpython-311.pyc
│       └── Server.cpython-311.pyc
│
├── db.sqlite3
├── manage.py
├── README.md
└── .gitignore



# MODIICAÇÕES ALISSON

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