from django.shortcuts import render

def generator(request):
    return render(request, 'events/inprogress.html',)


def raiting(request):
    return render(request, 'events/inprogress.html')

def myprofile(request):
    return render(request, 'events/inprogress.html')