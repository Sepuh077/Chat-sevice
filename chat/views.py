from django.shortcuts import render


def room(request, group_id):
    return render(request, 'chat/room.html', {
        'group_id': group_id
    })
