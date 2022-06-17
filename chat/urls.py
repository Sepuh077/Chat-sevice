from django.urls import path
from .views import *


urlpatterns = [
    path('', chat_home, name='chat-home'),
    path('<str:group_id>/', room, name='room'),
]