from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse


from .forms import *


def login_user(request):

    nextpage = request.GET.get("next", reverse('index'))
    backpage = request.META.get('HTTP_REFERER', 'index')



    if request.user.is_authenticated:
        return redirect(nextpage)

    if request.method == "POST":

        form = LoginUserForm(request.POST)

        try:
            user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
            if user is not None:
                login(request, user)
                return redirect(nextpage)
            else:
                form.add_error(None, "Данные неверны")
        except:
            form.add_error(None, "Произошла неизвестная ошибка")
    else:
        form = LoginUserForm()

    return render(request, 'users/login.html', {'nextto': nextpage, 'forms': form, "backto": backpage})
def logout_user(request):

    nextpage = request.GET.get("next", reverse('index'))

    if request.user.is_authenticated:
        logout(request)
    return redirect(nextpage)


def only_staff(f):

    def checking(request, *args, **kwargs):
        if request.user.is_staff:
            return f(request, *args, **kwargs)
        elif request.user.is_anonymous:
            return redirect(reverse('login')+"?next="+request.path)
        else:
            return redirect(request.META.get('HTTP_REFERER', 'index'))
    return checking

@login_required
def profile(request):

    return render(request, 'users/profile.html')