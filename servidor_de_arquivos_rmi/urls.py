"""
URL configuration for servidor_de_arquivos_rmi project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf.urls.static import static 
from django.contrib import admin
from django.urls import path
from cliente_rmi.views import Visualizar_arquivos, Enviar_arquivos, Deletar_arquivo, Download_arquivo

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',Visualizar_arquivos.as_view(), name='visualizar_arquivos'),
    path('files/',Visualizar_arquivos.as_view(), name='visualizar_arquivos'),
    path('upload/',Enviar_arquivos.as_view(), name='enviar_arquivo'),
    path('download/<str:nome_arquivo>',Download_arquivo.as_view, name='download_arquivo'),
    path('delete/<str:nome_arquivo>',Deletar_arquivo.as_view, name='deletar_arquivo'),
]
