from django.shortcuts import render


def chat_home(request):
    
    context = {}
    
    return render(request, 'chat/home.html', context)


def room(request, group_id):
    
    context = {
        'group_id': group_id
    }
    return render(request, 'chat/room.html', context)


def get_profiles(request):
    pass
