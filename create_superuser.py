import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

try:
    django.setup()
    from django.contrib.auth import get_user_model
    User = get_user_model()

    USERNAME = 'dino'
    EMAIL = 'dino@example.com'
    PASSWORD = 'solosolinsolito'  # Usa la contraseña que tú quieras aquí

    user, created = User.objects.get_or_create(username=USERNAME, defaults={'email': EMAIL})
    user.set_password(PASSWORD)
    user.is_superuser = True
    user.is_staff = True
    user.save()
    print("Superusuario configurado correctamente.")
except Exception as e:
    print(f"Error al crear superusuario: {e}")