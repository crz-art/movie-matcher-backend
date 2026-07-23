from django.db import models

# Tabla 1: Géneros cinematográficos
class Genero(models.Model):
    nombre_genero = models.CharField(max_length=50)  # Tipo: VARCHAR

    def __str__(self):
        return self.nombre_genero

# Tabla 2: Usuarios de la plataforma
class Usuario(models.Model):
    nombre = models.CharField(max_length=100)        # Tipo: VARCHAR
    correo = models.EmailField(unique=True)          # Tipo: VARCHAR
    fecha_registro = models.DateTimeField(auto_now_add=True) # Tipo: DATETIME

    def __str__(self):
        return self.nombre

# Tabla 3: Películas
class Pelicula(models.Model):
    titulo = models.CharField(max_length=150)        # Tipo: VARCHAR
    duracion = models.IntegerField()                 # Tipo: INT (minutos)
    nivel_adrenalina = models.IntegerField()         # Tipo: INT (escala 1 a 5)
    poster_url = models.CharField(max_length=300)    # Tipo: VARCHAR
    genero = models.ForeignKey(Genero, on_delete=models.CASCADE, related_name='peliculas') # Llave foránea (FK)

    def __str__(self):
        return self.titulo

# Tabla 4: Watchlist (Películas guardadas por cada usuario)
class Watchlist(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='watchlist') # FK
    pelicula = models.ForeignKey(Pelicula, on_delete=models.CASCADE)                          # FK
    agregado_en = models.DateTimeField(auto_now_add=True)                                     # Tipo: DATETIME

    def __str__(self):
        return f"{self.usuario.nombre} - {self.pelicula.titulo}"