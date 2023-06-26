# python_food_api

python3 -m venv delenv
source delenv/bin/activate
pip install django
pip install djangorestframework
django-admin startproject food .
pip install python-decouple

# Create .env file and input
SECRET_KEY = c6514df202d709283de90939
DEBUG = True

AND in settings.py 

from decouple import config

SECRET_KEY = config('SECRET_KEY')
DEBUG = config('DEBUG', cast=bool)

To do above change command in Terminal

python
>>> import secrets
>>> secrets.token_hex(12)
'c6514df202d709283de90939'






Now, Create apps

 python3 manage.py startapp auth
python3 manage.py startapp orders

To save all in a file
pip3 freeze > requirements.txt

For phone number field need to command
pip install "django-phonenumber-field[phonenumbers]"

To auth, set it into setting.py
AUTH_USER_MODEL ='authentication.User'

For JWT:
https://djoser.readthedocs.io/en/latest/getting_started.html#supported-authentication-backends

pip install -U djoser
pip install -U djangorestframework_simplejwt

Configure INSTALLED_APPS:

INSTALLED_APPS = (

    'djoser',
)
REST_FRAMEWORK={
"NON_FIELD_ERRORS_KEY":"error",
"DEFAULT_AUTHENTICATION_CLASSES":(
'rest_framework_simplejwt.authentication.JWTAuthentication',
)
}

from datetime import timedelta


SIMPLE_JWT = {
'AUTH_HEADER_TYPES': ('Bearer',),
"ACCESS_TOKEN_LIFETIME": timedelta(minutes=5),
"REFRESH_TOKEN_LIFETIME": timedelta(days=1),
}

And url.py
urlpatterns = [
…….
path('auth/', include('djoser.urls.jwt')),
]






For Documentation:
https://drf-yasg.readthedocs.io/en/stable/readme.html

pip install -U drf-yasg

In settings.py:

INSTALLED_APPS = [
   ...
   'django.contrib.staticfiles',  # required for serving swagger ui's css/js files
   'drf_yasg',
   ...
]

SWAGGER_SETTINGS = {
   'SECURITY_DEFINITIONS': {
      'Basic': {
            'type': 'basic'
      },
      'Bearer': {
            'type': 'apiKey',
            'name': 'Authorization',
            'in': 'header'
      }
   }
}


In urls.py:
...
from django.urls import re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

...

schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
   path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
   path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
   ...
]

For database:
https://pypi.org/project/dj-database-url/

pip install dj-database-url

For Doc Static:
https://whitenoise.readthedocs.io/en/latest/

pip install whitenoise

Edit your settings.py file and add WhiteNoise to the MIDDLEWARE list, above all other middleware apart from Django’s SecurityMiddleware:
MIDDLEWARE = [
    # ...
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    # ...
]
Want forever-cacheable files and compression support? Just add this to your settings.py:
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"



