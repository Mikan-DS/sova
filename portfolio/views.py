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
    students = {std: 0 for std in Student.objects.all()}
    for std in students.keys():
        students[std] = sum(i['achievement__score'] for i in Document.objects.filter(activity__student=std).values('achievement__score'))

    def sorter(item):
        return item[1]

    ratings = [(place+1, i, j) for place, (i, j) in enumerate(sorted(students.items(), key=sorter, reverse=True))]


    return render(request, 'portfolio/raiting.html', {'ratings': ratings})

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

def achievement_wall(request):
    return render(request, 'portfolio/achievement_wall.html', {'documents': Document.objects.filter(achievement__nomination_id__in=[1, 2])})