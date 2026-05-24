#!/usr/bin/env bash
# Salir de inmediato si ocurre un error
set -o errexit

echo "=== INSTALANDO DEPENDENCIAS ==="
pip install --upgrade pip
pip install -r requirements.txt

echo "=== RECOPILANDO ARCHIVOS ESTÁTICOS ==="
python manage.py collectstatic --noinput

echo "=== APLICANDO MIGRACIONES ==="
python manage.py migrate

echo "=== CREANDO SUPERUSUARIO ENCRIPTADO ==="
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
    print('Superusuario creado exitosamente.')
else:
    print('El superusuario ya existía.')
"
echo "=== BUILD COMPLETADO CON ÉXITO ==="