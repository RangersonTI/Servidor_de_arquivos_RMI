from django.db import models

class Enviar_Arquivo(models.Model):
    nome_arquivo = models.CharField(max_length=100)
    url_arquivo = models.URLField()
    data_upload = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome_arquivo