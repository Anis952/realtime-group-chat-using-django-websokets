import os

from channels.routing import ProtocolTypeRouter,URLRouter
from django.core.asgi import get_asgi_application
import chat.consumers
from channels.auth import AuthMiddlewareStack
from django.urls import path

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websockets" : AuthMiddlewareStack(URLRouter([path('ws/chat/<int:room_name/',chat.consumers.ChatConsumer.as_asgi)]))
    # Just HTTP for now. (We can add other protocols later.)
})


