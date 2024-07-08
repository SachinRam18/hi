# myproject/asgi.py
import os
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from django.core.asgi import get_asgi_application
from users.routing import websocket_urlpatterns  # Import your websocket_urlpatterns from users.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')

application = ProtocolTypeRouter({
    'http': get_asgi_application(),  # HTTP protocol handler
    'websocket': AuthMiddlewareStack(  # WebSocket protocol handler with authentication middleware
        URLRouter(
            websocket_urlpatterns  # Routing for WebSocket paths
        )
    ),
})
