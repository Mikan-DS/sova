from django.contrib.auth.models import User

from appeals.models import Message


def get_all_chats():
    return {i['user'] for i in Message.objects.all().values('user')}
