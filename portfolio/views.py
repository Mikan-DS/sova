from django.shortcuts import render

def generator(request):
    return render(request, 'events/inprogress.html',)
