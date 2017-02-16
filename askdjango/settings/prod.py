from .common import *

DEBUG = True

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

DATABASES = {
    'defaults' : {
        'ENGINE' : 'django.db.backends.mysql',
        'HOST' : 'gustos.mysql.pythonanywhere-services.com',
        'NAME' : 'gustos$dafault',
        'USER' : 'gustos',
        'PASSWORD' : 'akwjd123',
        'OPTIONS' : {
            'ssql_mode' : 'traditional',
        }
    }
}
