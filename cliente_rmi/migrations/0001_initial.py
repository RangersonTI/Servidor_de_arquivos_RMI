# Generated by Django 5.0.6 on 2024-06-19 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Enviar_Arquivo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_arquivo', models.CharField(max_length=100)),
                ('arquivo', models.FileField(upload_to='uploads/')),
                ('data_upload', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
