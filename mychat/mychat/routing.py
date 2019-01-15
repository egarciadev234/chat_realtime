from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
import chat.routing
"""
    Esta configuracion de enrutamiento especifica e inspecciona el tipo de conexion antes de 
    conectarse al servidor de desarrollo de canales

"""
application = ProtocolTypeRouter({
    'websocket': AuthMiddlewareStack(
        URLRouter(
            chat.routing.websocket_urlpatterns
        )
    ),
})