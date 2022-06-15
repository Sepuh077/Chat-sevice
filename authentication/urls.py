from django.urls import path
from .views import login, register, logout, authentication


urlpatterns = [
    path('login/', authentication, name='login'),
    path('logout/', logout, name='logout'),
    path('register/', authentication, name='register'),
]
