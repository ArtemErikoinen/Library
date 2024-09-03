from pathlib import Path
from import_export.formats.base_formats import XLSX

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = 'django-insecure-7x3lh_4c$h*33r$v^5us0qrmhqx*#k&(p1@7u&+b7tl!&^tvt('


DEBUG = False

ALLOWED_HOSTS = ['127.0.0.1', 'localhost']
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'book',
        'USER': 'postgres',
        'PASSWORD': '12345678',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

STATIC_URL = 'static/'
