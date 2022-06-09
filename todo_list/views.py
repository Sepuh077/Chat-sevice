from django.http import JsonResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import requests
import re


# Create your views here.
@login_required(login_url='/login/')
def dashboard(request):
    context = {}
    return render(request, 'todo/dashboard.html', context)


@login_required(login_url='/login/')
def get_google_images(request):
    data = {
        'images': [],
        'name': ''
    }
    if request.method == "GET":
        name = request.GET.get('name', '')
        data['name'] = name
        content = str(requests.get(f'https://www.google.com/search?q={name}&sxsrf=ALiCzsa5T0S4U4xLg6O1ajVtvYb6MjYthQ:1654799296002&source=lnms&tbm=isch&sa=X&ved=2ahUKEwiVxNnh_6D4AhWJR_EDHUDmBR0Q_AUoAXoECAIQAw&biw=1848&bih=968&dpr=1').content)
        data['images'] = re.findall(r'<img.*src="([^"]*)"', content)[:10]
    
    return JsonResponse(data)
