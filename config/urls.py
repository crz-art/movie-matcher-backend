from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from core.views import GeneroViewSet, UsuarioViewSet, PeliculaViewSet, WatchlistViewSet

router = DefaultRouter()
router.register(r'generos', GeneroViewSet)
router.register(r'usuarios', UsuarioViewSet)
router.register(r'peliculas', PeliculaViewSet)
router.register(r'watchlist', WatchlistViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
