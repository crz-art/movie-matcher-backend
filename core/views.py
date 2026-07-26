from rest_framework import viewsets
from .models import Genero, Usuario, Pelicula, Watchlist
from .serializers import (
    GeneroSerializer,
    UsuarioSerializer,
    PeliculaSerializer,
    WatchlistSerializer,
)

class GeneroViewSet(viewsets.ModelViewSet):
    queryset = Genero.objects.all()
    serializer_class = GeneroSerializer


class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer


class PeliculaViewSet(viewsets.ModelViewSet):
    serializer_class = PeliculaSerializer

    def get_queryset(self):
        queryset = Pelicula.objects.all()
        genero_id = self.request.query_params.get('genero')
        if genero_id:
            queryset = queryset.filter(genero_id=genero_id)
        return queryset


class WatchlistViewSet(viewsets.ModelViewSet):
    queryset = Watchlist.objects.all()
    serializer_class = WatchlistSerializer