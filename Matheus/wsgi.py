import os
from django.core.wsgi import get_wsgi_application
from whitenoise import WhiteNoise

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Matheus.settings')
application = get_wsgi_application()
application = WhiteNoise(application, root="/caminho/para/arquivos/estaticos")
application.add_files("/caminho/para/mais/arquivos/estaticos", prefix="mais-arquivos/")
