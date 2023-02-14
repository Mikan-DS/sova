from django import template

from .models import *


def get_all_years():
    try:
        return sorted({i['year'] for i in Plan.objects.all().values('year')})
    except:
        return []

# def get_all_years():
#     return sorted({i for i in Plan.objects.all().values('year')})

def get_all_months_str():
    return [Month.objects.get(pk=i).title for i in
            sorted({i['month_id'] for i in Plan.objects.all().values('month_id')})]


def get_all_months():
    try:
        return sorted({i['month_id'] for i in Plan.objects.all().values('month_id')})
    except:
        return []


def int_choices(__iter):
    return [(str(i), str(i)) for i in __iter]


def model_choices(__iter, model):
    return {(str(i), str(model.objects.get(pk=i))) for i in __iter}


def model_choices_dict(__iter, model):
    return {str(model.objects.get(pk=i)): i for i in __iter}


def int_choices_dict(__iter):
    return {str(i): i for i in __iter}

