from .models import Profile


def get_profile_by_id(profile_id):
    try:
        return Profile.objects.get(id=profile_id)
    except Exception as exc:
        print(exc)
        return None
