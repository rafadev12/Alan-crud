#!/usr/bin/env bash
# Salir si ocurre un error
set -o errexit

# Instalar dependencias
pip install -r requirements.txt

# Recopilar archivos estáticos
python manage.py collectstatic --noinput

# Aplicar migraciones a la base de datos de producción
python manage.py migrate

# Crear el superusuario automáticamente sin pedir datos por consola
python -c "
import django
django.setup()
from django.contrib.auth import get_user_model
User = get_user_model()
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@admin.com', 'AlanPassword2026')
    print('Superusuario creado exitosamente')
else:
    print('El superusuario ya existe')
"