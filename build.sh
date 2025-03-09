pip install -r requirements.txt
python manage.py migrate
python manage.py collectstatic --noinput

echo "
from django.contrib.auth import get_user_model
User = get_user_model()
if not User.objects.filter(correo='superuser@gmail.com').exists():
    User.objects.create_superuser(correo='superuser@gmail.com', password='s123456789_', nombre_usuario='Superuser')
    print('Superuser creado exitosamente.')
else:
    print('El superusuario ya existe.')
" | python manage.py shell