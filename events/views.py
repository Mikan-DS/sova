from django.forms import model_to_dict
from django.shortcuts import render, redirect

from .models import *
from .forms import *


def index(request):
    return render(request, 'events/index.html')

def events(request):
    all_events = Event.objects.all()
    return render(request, 'events/events.html', {'events': all_events})

def event(request, event_id):
    c_event = Event.objects.get(pk=event_id)
    plans = Plan.objects.filter(event_id=event_id)
    return render(request, 'events/event.html', {
        'event': c_event,
        'type': c_event.event_type,
        'level': c_event.event_level,
        'weorg': "Организаторы" if c_event.weorg else 'Участники',
        'plans': plans

    })

def create_event(request):
    if request.method == "POST":
        form = ModifyEvent(request.POST)
        if form.is_valid():
            # print(form.cleaned_data)
            try:
                e = Event.objects.create(**form.cleaned_data)
                return redirect(e.get_absolute_url())
            except:
                form.add_error(None, "Произошла ошибка при добавлении мероприятия.")


    else:
        form = ModifyEvent()
    return render(request, 'events/create_event.html', {'form': form})

def edit_event(request, event_id):
    e = Event.objects.get(pk=event_id)
    if request.method == "POST":
        form = ModifyEvent(request.POST)
        if form.is_valid():
            # print(form.cleaned_data)
            try:
                # e = Event.objects.create(**form.cleaned_data)
                e.title = form.cleaned_data['title']
                e.description = form.cleaned_data['description']
                e.event_type = form.cleaned_data['event_type']
                e.event_level = form.cleaned_data['event_level']
                e.weorg = form.cleaned_data['weorg']
                e.save()
                return redirect(e.get_absolute_url())
            except:
                form.add_error(None, "Произошла ошибка при обновлении мероприятия.")


    else:
        form = ModifyEvent(initial=model_to_dict(e))

    return render(request, 'events/edit_event.html', {'form': form, 'event_id': event_id})

def delete_event(request, event_id):
    e = Event.objects.get(pk=event_id)
    e.delete()
    return redirect('events')



def add_plan(request, event_id):
    if request.method == "POST":
        form = ModifyPlan(request.POST)
        if form.is_valid():
            try:
                p = Plan.objects.create(**form.cleaned_data, event_id=event_id)
                return redirect(p.get_absolute_url())
            except:
                form.add_error(None, "Произошла ошибка при добавлении плана у мероприятия.")

    else:
        form = ModifyPlan()
    return render(request, 'events/create_plan.html', {'form': form, 'event_id':event_id})

def plan(request, event_id, plan_id):
    c_plan = Plan.objects.get(pk=plan_id)

    result = Result.objects.filter(plan_id=plan_id)

    return render(request, 'events/plan.html', {
        'plan': c_plan,
        'type': c_plan.event.event_type,
        'level': c_plan.event.event_level,
        'weorg': "Организаторы" if c_plan.event.weorg else 'Участники',
        'result': result[0] if result else False

    })

def plans(request):
    all_events = Plan.objects.all()
    return render(request, 'events/plans.html', {'plans': all_events})

def raiting(request):
    return render(request, 'events/inprogress.html')

def myprofile(request):
    return render(request, 'events/inprogress.html')

