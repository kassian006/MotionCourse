from django.urls import path
from .consumers import ChatConsumer#, VideoCallConsumer, AudioCallConsumer

websocket_urlpatterns = [
    path('ws/chat/<str:room_name>/', ChatConsumer.as_asgi()),
    # re_path(r'ws/chat/(?P<room_name>\w+)/$', ChatConsumer.as_asgi()),
    # path('ws/call/<str:room_name>/', VideoCallConsumer.as_asgi()),
    # re_path(r'ws/call/(?P<room_name>\w+)/$', VideoCallConsumer.as_asgi()),
    # path('ws/audio/<str:room_name>/', AudioCallConsumer.as_asgi()),
    # re_path(r'ws/audio/(?P<room_name>\w+)/$', AudioCallConsumer.as_asgi()),

]
