from django.http import JsonResponse
from django.shortcuts import redirect, render
from authentication.manager import get_profile_by_id
from .manager import *
from django.contrib.auth.decorators import login_required


@login_required(login_url='/login/')
def chat_home(request):
    
    context = {
        'groups': get_user_groups_info(request.user)
    }
    
    return render(request, 'chat/room.html', context)


@login_required(login_url='/login/')
def room(request, group_id):
    group = get_group_by_id(group_id)
    if not group or not group.members.contains(request.user):
        return redirect('chat-home')
    
    context = {
        'group_id': group_id,
        'groups': get_user_groups_info(request.user),
        'messages_data': get_group_messages(group)
    }
    return render(request, 'chat/room.html', context)


@login_required(login_url='/login/')
def redirect_to_personal_chat(request, profile_id):
    profile = get_profile_by_id(profile_id)
    if not profile:
        return redirect('chat-home')
    group = get_personal_group_by_users(request.user, profile)
    if group:
        return redirect('room', group_id=group.id)
    return redirect('room', group_id=create_personal_group(request.user, profile).id)


@login_required(login_url='/login/')
def get_profiles(request, search_text):
    if request.method == "GET":
        data = get_profiles_by_text(search_text, request.user.id)
    else:
        data = []

    return JsonResponse(data, safe=False)
