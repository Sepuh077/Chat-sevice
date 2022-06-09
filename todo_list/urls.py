from django.urls import path
from .views import *


urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('get-google-images/', get_google_images),
]
