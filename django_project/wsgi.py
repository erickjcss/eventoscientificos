import os
from django.core.wsgi import get_wsgi_application
from whitenoise import DjangoWhiteNoise

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_project.settings')

application = DjangoWhiteNoise(get_wsgi_application())
