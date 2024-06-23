from django.db import models
import os
from django.db.models.signals import post_delete
from django.dispatch import receiver

class Enviar_Arquivo(models.Model):
    nome_arquivo = models.CharField(max_length=100)
    arquivo = models.FileField( upload_to='uploads/')  # Define a pasta onde os arquivos serão armazenados
    data_upload = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome_arquivo

    @classmethod
    def adicionar_arquivo(cls,nome_arquivo,arquivo):
        novo_arquivo = cls(nome_arquivo=nome_arquivo,arquivo=arquivo)
        novo_arquivo.save()
        return novo_arquivo

    def remover_arquivo(self):
        if os.path.isfile(self.arquivo.path):
            os.remove(self.arquivo.path)
        self.delete()

@receiver(post_delete, sender=Enviar_Arquivo)
def deletar_arquivo(sender, instance, **kwargs):
    # Verifica se o arquivo existe e o remove
    if instance.arquivo and os.path.isfile(instance.arquivo.path):
        os.remove(instance.arquivo.path)