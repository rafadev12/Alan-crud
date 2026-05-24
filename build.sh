# Crear el superusuario de Django con contraseña encriptada correctamente
python -c "
import django
django.setup()
from django.contrib.auth import get_user_model
User = get_user_model()
if not User.objects.filter(username='admin').exists():
    user = User.objects.create_user('admin', 'admin@admin.com', 'AlanPassword2026')
    user.is_staff = True
    user.is_superuser = True
    user.save()
    print('Superusuario encriptado creado exitosamente')
else:
    print('El superusuario ya existe')
"