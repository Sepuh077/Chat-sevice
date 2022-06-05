from django.shortcuts import render
from .models import Profile


# Create your views here.
def login(request):
    return render(request, 'authentication/login.html')