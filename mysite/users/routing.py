# from django.urls import path
# from .consumers import ChatConsumer
#
# websocket_urlpatterns = [
#     path('ws/chat/<str:room_name>/', ChatConsumer.as_asgi()),
#
# ]

# routing.py
from django.urls import re_path
from . import consumers

websocket_urlpatterns = [
    re_path(r'ws/chat/(?P<room_name>\w+)/$', consumers.ChatConsumer.as_asgi()),
]