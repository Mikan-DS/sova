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

        form = LoginUserForm(data=request.POST)

        if form.is_valid():
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

    return render(request, 'users/profile.html')\

@login_required
def edit_profile(request):
    if request.method == "POST":
        form = ChangeUser(request.POST, request.FILES or None)
        # print(form.cleaned_data['number'])

        if form.is_valid():

            try:
                request.user.email = form.cleaned_data['email']
                request.user.student.number = '+7'+form.cleaned_data['number'][-10:]
                if form.cleaned_data['image']:

                    request.user.student.image = form.cleaned_data['image']
                request.user.save()
                request.user.student.save()

                return redirect('profile')
            except:
                pass

    else:
        form = ChangeUser(initial={"number": request.user.student.number, "email": request.user.email})

    return render(request, 'users/edit_profile.html', {'form': form})