from django.urls import path
from .views import *


urlpatterns = [
    path('', chat_home, name='chat-home'),
    path('<str:group_id>/', room, name='room'),
    path('get-profiles/search=<str:search_text>/', get_profiles, name='get-profiles'),
]