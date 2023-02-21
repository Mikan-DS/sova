from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from users.views import only_staff
from .forms import *
from .models import *
from .utils import get_all_chats, get_all_last_messages


@login_required
def write_to_admin(request):
    if request.method == "POST":
        try:
            Message.objects.create(by_moderator=False, content=request.POST.get('content'), user=request.user)
            return redirect('ask moderator')
        except:
            pass
    form = WriteMessage()
    return render(
        request,
        'appeals/write_to_admin.html',
        {
            'messages': Message.objects.filter(user=request.user),
            'form': form
        })
@only_staff
def appeals(request):
    return render(
        request,
        'appeals/all_chats.html',
        {
            'chats': get_all_last_messages()
        })
@only_staff
def answer_to_user(request, user_id):
    user = User.objects.get(pk=user_id)
    if request.method == "POST":
        try:
            Message.objects.create(by_moderator=True, content=request.POST.get('content'), user=user)
            return redirect('answer user', {'user_id': user_id})

        except:
            pass
    form = WriteMessage()
    return render(
        request,
        'appeals/answer_to_user.html',
        {
            'messages': Message.objects.filter(user=user),
            'form': form,
            'student': user
        })
