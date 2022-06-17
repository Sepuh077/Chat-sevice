from authentication.models import Profile
from django.db.models import Q


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
