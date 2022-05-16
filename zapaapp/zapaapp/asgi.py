"""
ASGI config for zapaapp project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

import os
import django

#from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter # para el chat
from channels.http import AsgiHandler # para el chat -> versiones en conflicto: "django >=2.2 no longere has inbuilt ASGI support..."
# por suerte channels presenta una alternativa

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'zapaapp.settings')
django.setup()


#application = #get_asgi_application()
application = ProtocolTypeRouter({
    'http': AsgiHandler(),        #get_asgi_application(),
})
