from django.urls import path
from .views import *


urlpatterns = [
    path('<str:group_id>/', room, name='room'),
]