from django.db import models


# Create your models here.
class Livro(models.Model):
    # tipo de caracter de no maximo 200 caracteres
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    # inteiro
    paginas = models.IntegerField()
    editora = models.CharField(max_length=50)
    edicao = models.IntegerField()
    ano_publicacao = models.IntegerField()
    idioma = models.CharField(max_length=20)
    isbm = models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.titulo
