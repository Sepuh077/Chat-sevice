from django.http import JsonResponse
from django.shortcuts import render
from authentication.models import Profile
from .manager import get_profiles_by_text
from django.contrib.auth.decorators import login_required


@login_required(login_url='/login/')
def chat_home(request):
    
    context = {}
    
    return render(request, 'chat/room.html', context)


@login_required(login_url='/login/')
def room(request, group_id):
    
    context = {
        'group_id': group_id
    }
    return render(request, 'chat/room.html', context)


@login_required(login_url='/login/')
def get_profiles(request, search_text):
    if request.method == "GET":
        data = get_profiles_by_text(search_text, request.user.id)
    else:
        data = []

    return JsonResponse(data, safe=False)
