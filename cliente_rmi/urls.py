from django.urls import path
from django.contrib import admin
from .views import Visualizar_arquivos, Enviar_arquivos, Deletar_arquivo, Download_arquivo

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',Visualizar_arquivos.as_view(), name='visualizar_arquivos'),
    path('files/',Visualizar_arquivos.as_view(), name='visualizar_arquivos'),
    path('upload/',Enviar_arquivos.as_view(), name='enviar_arquivo'),
    path('download/<str:nome_arquivo>',Download_arquivo.as_view, name='download_arquivo'),
    path('delete/<str:nome_arquivo>',Deletar_arquivo.as_view, name='deletar_arquivo'),
]