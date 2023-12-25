from .base import *
# SECURITY WARNING: don't run with debug turned on in production!



# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'groupone$default',
        'USER': 'groupone',
        'PASSWORD': 'informatorio2023',
        'HOST': 'groupone.mysql.pythonanywhere-services.com',
        'PORT': '',
    }
}