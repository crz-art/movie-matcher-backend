from rest_framework import serializers
from .models import Genero, Usuario, Pelicula, Watchlist

class GeneroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genero
        fields = '__all__'

class PeliculaSerializer(serializers.ModelSerializer):
    genero_nombre = serializers.ReadOnlyField(source='genero.nombre_genero')

    class Meta:
        model = Pelicula
        fields = ['id', 'titulo', 'duracion', 'nivel_adrenalina', 'poster_url', 'genero', 'genero_nombre']

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'

class WatchlistSerializer(serializers.ModelSerializer):
    pelicula_detalle = PeliculaSerializer(source='pelicula', read_only=True)

    class Meta:
        model = Watchlist
        fields = ['id', 'usuario', 'pelicula', 'pelicula_detalle', 'agregado_en']
