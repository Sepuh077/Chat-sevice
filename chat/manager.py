from authentication.models import Profile
from authentication.manager import get_profile_by_id
from django.db.models import Q
from .models import *


def get_profiles_by_text(text, my_id):
    return [
        {
            'id': profile.id,
            'email': profile.email,
            'name': profile.name,
            'image': profile.profile_img.url,
        }
        for profile in Profile.objects.filter(
            Q(name__icontains=text) |
            Q(email__icontains=text)
        ).exclude(id__in=[my_id])
    ]
    

def get_group_by_id(group_id):
    try:
        return Group.objects.get(id=group_id)
    except Exception:
        return None


def get_personal_groups():
    return Group.objects.filter(is_personal=True)


def get_personal_group_by_users(user1, user2):
    return Group.objects.filter(is_personal=True, members=user1).filter(members=user2).first()


def create_personal_group(user1, user2):
    group = Group.objects.create()
    group.members.add(user1, user2)
    return group


def get_user_groups(user):
    return Group.objects.filter(members=user).order_by('-is_personal')


def get_group_data(user, group):
    if group.is_personal:
        profile = group.members.all().exclude(id=user.id).first()
        return {
            'id': group.id,
            'name': profile.name,
            'picture': profile.profile_img.url
        }
    else:
        return {
            'id': group.id,
            'name': group.name,
            'picture': group.picture.url
        }


def get_user_groups_info(user):
    groups = get_user_groups(user)
    info = []
    for group in groups:
        info.append(get_group_data(user, group))
    
    return info


def create_text_message(sender_id, group_id, text):
    if not text:
        return
    sender = get_profile_by_id(sender_id)

    if not sender:
        return
    group = get_group_by_id(group_id)

    if not group:
        return
    message = Message.objects.create(
        sender=sender,
        receiver=group
    )
    TextMessage.objects.create(
        message=message,
        text=text
    )
    

def get_message_data(message):
    text_msg = TextMessage.objects.filter(message=message).first()
    
    return {
        'id': message.id,
        'sender': {
            'id': message.sender.id,
            'name': message.sender.name,
            'picture': message.sender.profile_img,
        },
        'sent_time': message.sent_time,
        'text': text_msg.text
    } if text_msg else None
    

def get_group_messages(group):
    messages = Message.objects.filter(receiver=group).order_by('-sent_time')
    data = []
    for message in messages:
        message_data = get_message_data(message)
        if message_data:
            data.append(message_data)

    return data
