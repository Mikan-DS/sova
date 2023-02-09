from django.shortcuts import render

from .models import *


def index(request):
    return render(request, 'events/index.html')

def events(request):
    all_events = Event.objects.all()
    return render(request, 'events/events.html', {'events': all_events})

def event(request, event_id):
    c_event = Event.objects.get(pk=event_id)
    return render(request, 'events/event.html', {
        'event': c_event,
        'type': c_event.event_type,
        'level': c_event.event_level,
        'weorg': "Организаторы" if c_event.weorg else 'Участники',

    })