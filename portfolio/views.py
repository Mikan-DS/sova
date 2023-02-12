from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse

from events.models import Plan, update_model_from_dict
from users.views import only_staff
from .forms import *
from .models import *


def generator(request):
    return render(request, 'events/inprogress.html',)


def raiting(request):
    return render(request, 'events/inprogress.html')

@login_required
def portfolio(request):


    form = AddDocument(request.POST or None, request.FILES or None)
    form.fields['activity'].queryset = Activity.objects.filter(student=request.user.student)

    if form.is_valid():
        doc = Document()
        update_model_from_dict(doc, form.cleaned_data)
        doc.save()

    return render(request, 'portfolio/portfolio.html', {'form': form, 'documents': Document.objects.filter(activity__student=request.user.student)})

@only_staff
def edit_peoples_on_shedule(request, plan_id):
    return render(request, 'portfolio/choice_add_method.html', {'plan_id': plan_id, 'activities': Activity.objects.filter(shedule__plan_id=plan_id)})

@only_staff
def delete_student_from_plan(request, activity_id):
    try:
        activity = Activity.objects.get(pk=activity_id)
        activity.delete()
    except Exception as e:
        print(repr(e))
    return redirect('index')
@only_staff
def edit_peoples_byhand(request, plan_id):
    form = AddStudent(request.POST or None)
    plan = Plan.objects.get(pk=plan_id)
    if form.is_valid():
        print(Activity.objects.get_or_create(shedule=plan.shedule, student=form.cleaned_data['student'], event_role=form.cleaned_data['event_role']))
    return render(request, 'portfolio/add_byhand.html', {'plan_id': plan_id, 'activities': Activity.objects.filter(shedule__plan_id=plan_id), 'form': form})