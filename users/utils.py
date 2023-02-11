from django.contrib.auth.models import User


def is_user_in_group(request, group):
    try:
        assert request.groups.get(pk=group)
        return True
    except:
        return False

def is_user_mod(request):
    return is_user_in_group(request, 1)