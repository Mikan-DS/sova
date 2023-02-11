import django.conf
from django.contrib.auth.decorators import login_required, permission_required
from django.forms import model_to_dict
from django.shortcuts import render, redirect
from django.utils import timezone

from users.views import only_staff
from .models import *
from .forms import *
from .utils import *


def index(request):

    reports = Report.objects.filter(created_at__gt=timezone.now()-datetime.timedelta(days=3)).order_by('created_at').reverse()[:3]


    return render(
        request,
        'events/index.html',
        {
            'reports': reports
        }
    )


#@login_required
@only_staff
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

@only_staff
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


@only_staff
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


@only_staff
def delete_event(request, event_id):
    e = Event.objects.get(pk=event_id)
    e.delete()
    return redirect('events')


@only_staff
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

    if shedule:
        reports = Report.objects.filter(shedule_id=c_plan.shedule.pk)
    else:
        reports = None

    return render(request, 'events/plan.html', {
        'plan': c_plan,
        'type': c_plan.event.event_type,
        'level': c_plan.event.event_level,
        'weorg': "Организаторы" if c_plan.event.weorg else 'Участники',
        'shedule': shedule,
        'reports': reports

    })


@only_staff
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


@only_staff
def delete_plan(request, event_id, plan_id):
    Plan.objects.get(pk=plan_id).delete()
    return redirect(Event.objects.get(pk=event_id).get_absolute_url())


@only_staff
def add_shedule(request, event_id, plan_id):
    p = Plan.objects.get(pk=plan_id)
    day = datetime.datetime.now()
    pday = datetime.datetime(p.year, p.month.pk, 1)
    day = day if day >= pday else pday
    Shedule.objects.get_or_create(plan_id=plan_id, begin=day, end=day)
    return redirect(p.get_absolute_url())


@only_staff
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


@only_staff
def create_report(request, plan_id, event_id=None,  report_id=None):
    plan = Plan.objects.get(pk=plan_id)

    report = Report.objects.get(pk=report_id) if report_id else Report(title=str(plan))

    if request.method == "POST":
        form = ModifyReport(request.POST)

        # print(form.cleaned_data)

        if form.is_valid():
            try:

                update_model_from_dict(report, form.cleaned_data)
                report.edited_at = datetime.datetime.now()
                report.shedule_id = plan.shedule.pk
                report.save()
                return redirect(plan.get_absolute_url())
            except:
                form.add_error(None, "Произошла неизвестная ошибка.")
    else:

        form = ModifyReport(initial=model_to_dict(report))

    return render(
        request,
        'events/modify_report.html',
        {
            'form': form,
            'plan': plan,
            'report_id': report_id,
            'action': "Обновить отчет" if report_id else "Создать отчет"
        }
    )

@only_staff
def edit_report(request, report_id):
    plan = Report.objects.get(pk=report_id).shedule.plan.pk
    return create_report(request, plan_id=plan, report_id=report_id)



def read_report(request, report_id):

    report = Report.objects.get(pk=report_id)

    returnto = "toplan" in request.GET

    if returnto:
        plan = report.shedule.plan
        returnto = reverse('plan', kwargs={'event_id': plan.event.pk, 'plan_id': plan.pk})

    images = ReportImage.objects.filter(report_id=report_id)


    return render(
        request,
        'events/report.html',
        {
            'returnto': returnto or reverse('index'),
            'report': report,
            'images': images
        }

    )

@only_staff
def delete_image(request, image_id):
    img = ReportImage.objects.get(pk=image_id)
    img.delete()
    return redirect(request.GET.get("returnto", img.report.get_absolute_url()))

@only_staff
def add_images(request, report_id):
    rprt = Report.objects.get(pk=report_id)
    images = ReportImage.objects.filter(report_id=report_id)


    if request.method == "POST":
        form = AddImage(request.POST, request.FILES or None)


        if form.is_valid():
            try:
                print(form.cleaned_data)
                img = ReportImage(report_id=report_id)
                update_model_from_dict(img, form.cleaned_data)
                img.save()
            except Exception as e:
                print(repr(e))
                form.add_error(None, "Произошла неизвестная ошибка.")
    else:

        form = AddImage()

    return render(
        request,
        'events/add_images_to_report.html',
        {
            'form': form,
            'plan': plan,
            'report': rprt,
            'images': images,
            'returnto': rprt.get_absolute_url()
        }
    )

def plans(request):
    # all_events = Plan.objects.filter(=[2023])
    # print(get_all_months())
    # if request.method == "GET":
    #     print(request.GET)
    #     print(dir(request.GET))
    #     filt = FilterPlans(initial={'year': request.GET.getlist('year'), 'month': request.GET.getlist('month')})
    #     try:
    #         print(**filt.cleaned_data)
    #     except:
    #         print(2)
    #
    # else:
    #     filt = FilterPlans(initial=(request.POST or None))
    filt = FilterPlans(initial={'year': request.GET.getlist('year'), 'month': request.GET.getlist('month')})

    _plans = Plan.objects.filter(year__in=request.GET.getlist('year'), month_id__in=request.GET.getlist('month')).order_by('year', 'month')

    return render(request, 'events/plans.html', {'filter': filt, 'plans': _plans})#, {'plans': all_events})

# def plans(request):
#
#     years = get_all_years()
#     months = get_all_months()
#
#     return render(request, 'events/plans.html', {'years': years})#, {'plans': all_events})
#
