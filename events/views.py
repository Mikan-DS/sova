import django.conf
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
                update_model_from_dict(e, form.cleaned_data)
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
    return render(request, 'events/create_plan.html', {'form': form, 'event': Event.objects.get(pk=event_id)})

def plan(request, event_id, plan_id):

    c_plan = Plan.objects.get(pk=plan_id)

    # shedules = Shedule.objects.filter(plan_id=plan_id)

    try:
        shedule = c_plan.shedule
    except:
        shedule = None

    reports = []

    return render(request, 'events/plan.html', {
        'plan': c_plan,
        'type': c_plan.event.event_type,
        'level': c_plan.event.event_level,
        'weorg': "Организаторы" if c_plan.event.weorg else 'Участники',
        'shedule': shedule

    })



def edit_plan(request, event_id, plan_id):
    p = Plan.objects.get(pk=plan_id)
    if request.method == "POST":
        form = ModifyPlan(request.POST)
        if form.is_valid():
            # print(form.cleaned_data)
            try:
                # e = Event.objects.create(**form.cleaned_data)
                update_model_from_dict(p, form.cleaned_data)
                p.save()
                return redirect(p.get_absolute_url())
            except:
                form.add_error(None, "Произошла ошибка при обновлении плана.")

    else:
        form = ModifyPlan(initial=model_to_dict(p))

    return render(
        request,
        'events/edit_plan.html',
        {
            'form': form,
            'event': Event.objects.get(pk=event_id),
            'plan': p
        }
    )

def delete_plan(request, event_id, plan_id):
    Plan.objects.get(pk=plan_id).delete()
    return redirect(Event.objects.get(pk=event_id).get_absolute_url())

def add_shedule(request, event_id, plan_id):
    p = Plan.objects.get(pk=plan_id)
    day = datetime.datetime.now()
    pday = datetime.datetime(p.year, p.month.pk, 1)
    day = day if day >= pday else pday
    Shedule.objects.get_or_create(plan_id=plan_id, begin=day, end=day)
    return redirect(p.get_absolute_url())

def edit_shedule(request, event_id, plan_id):
    shedule = Shedule.objects.get(plan_id=plan_id)
    if request.method == "POST":
        form = ModifyShedule(request.POST)
        if form.is_valid():
            # print(form.cleaned_data)
            try:
                # e = Event.objects.create(**form.cleaned_data)
                update_model_from_dict(shedule, form.cleaned_data)
                shedule.save()
                return redirect(shedule.plan.get_absolute_url())
            except:
                form.add_error(None, "Произошла ошибка при обновлении плана.")
    else:
        form = ModifyShedule(initial=model_to_dict(shedule))

    return render(
        request,
        'events/edit_shedule.html',
        {
            'form': form,
            'event': Event.objects.get(pk=event_id),
            'plan': shedule
        }
    )


def plans(request):
    all_events = Plan.objects.all()
    return render(request, 'events/plans.html', {'plans': all_events})


