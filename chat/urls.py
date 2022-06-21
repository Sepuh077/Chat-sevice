from django.urls import path
from .views import *


urlpatterns = [
    path('redirect-to-personal-chat/<str:profile_id>/', redirect_to_personal_chat, name='redirect-to-personal-chat'),
    path('get-profiles/search=<str:search_text>/', get_profiles, name='get-profiles'),
    path('', chat_home, name='chat-home'),
    path('<int:group_id>/', room, name='room'),
]