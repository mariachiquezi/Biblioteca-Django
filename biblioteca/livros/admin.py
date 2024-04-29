from django.contrib import admin
from .models import Livro
# Register your models here.

# essa classe do adimin serve para a gente controlar paginação, quais atributos listar etc 
class ExibeLivro(admin.ModelAdmin):  
    # mostrar  
    list_display = ('id', 'titulo', 'ano_publicacao', 'isbm')  
    # links display posso clicar para acessar detalhes  
    list_display_links = ('id', 'titulo')  
    # buscar por titulo para achar na base de dados   
    search_fields = ('titulo',)    
    # filtrar pelo ano de publi
    list_filter = ('ano_publicacao',)  
    # paginar 2 livros por pagina  
    list_per_page = 2
admin.site.register(Livro, ExibeLivro)