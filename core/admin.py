from django.contrib import admin
from .models import Pelicula, Genero

@admin.register(Genero)
class GeneroAdmin(admin.ModelAdmin):
    pass  # Deja que Django muestre los campos automáticos de Género

@admin.register(Pelicula)
class PeliculaAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'nivel_adrenalina', 'duracion')
    list_display_links = ('id', 'titulo')  # 👈 Permite abrir la edición haciendo clic en el ID o en el Título
    search_fields = ('titulo',)