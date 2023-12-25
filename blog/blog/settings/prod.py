from .base import *
# SECURITY WARNING: don't run with debug turned on in production!



# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'Cecimaidana$default',
        'USER': 'Cecimaidana',
        'PASSWORD': 'informatorio2023',
        'HOST': 'Cecimaidana.mysql.pythonanywhere-services.com',
        'PORT': '',
    }
}