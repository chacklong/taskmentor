from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path
from monitoring import consumers

application = ProtocolTypeRouter({
    "websocket": URLRouter(
        [
            path("ws/progress/", consumers.TaskProgressConsumer.as_asgi()),
        ]
    )
})