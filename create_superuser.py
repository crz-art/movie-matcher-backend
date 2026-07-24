import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()

# Cambia estos datos por los que quieras usar para iniciar sesión
USERNAME = 'dino'
EMAIL = 'carlamart249@gmail.com'
PASSWORD = 'soyjochis12'

if not User.objects.filter(username=USERNAME).exists():
    User.objects.create_superuser(username=USERNAME, email=EMAIL, password=PASSWORD)
    print(f"Superusuario '{USERNAME}' creado exitosamente.")
else:
    print(f"El usuario '{USERNAME}' ya existe.")