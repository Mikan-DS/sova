from django.contrib.auth.models import User

from appeals.models import Message


def get_all_chats():
    return {i['user'] for i in Message.objects.all().values('user')}


def get_all_last_messages():
    usrs = []
    messages = []
    for message in Message.objects.all().order_by('sended_at').reverse():
        if not message.user in usrs:
            usrs.append(message.user)
            messages.append(message)
    return messages
