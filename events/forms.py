import datetime

from django import forms
from .models import *
from .utils import *


class ModifyEvent(forms.Form):
    title = forms.CharField(max_length=60, label="Название")
    description = forms.CharField(widget=forms.Textarea(attrs={'cols':60, 'rows': 10}), label="Описание")
    event_type = forms.ModelChoiceField(queryset=EventType.objects.all(), label="Тип мероприятия")
    event_level = forms.ModelChoiceField(queryset=EventLevel.objects.all(), label="Уровень мероприятия")
    weorg = forms.BooleanField(required=False, label="Организаторы", initial=True)

class ModifyPlan(forms.Form):
    year = forms.IntegerField(label="Год", initial=datetime.datetime.now().year)
    month = forms.ModelChoiceField(queryset=Month.objects.all(), label="Месяц", initial=datetime.datetime.now().month)

class ModifyShedule(forms.Form):
    begin = forms.DateField(label='Дата начала')
    end = forms.DateField(label='Дата конца')

class ModifyReport(forms.Form):
    title = forms.CharField(max_length=60, label="Название")
    content = forms.CharField(widget=forms.Textarea(attrs={'cols':60, 'rows': 10}), label="Описание")

class AddImage(forms.Form):
    image = forms.ImageField(label="Добавить изображение")


class FilterPlans(forms.Form):
    all_years = get_all_years()
    year = forms.ChoiceField(widget=forms.CheckboxSelectMultiple, choices=int_choices(all_years), label="Годы", required=False) #, initial=all_years
    months = get_all_months()
    month = forms.ChoiceField(widget=forms.CheckboxSelectMultiple, choices=model_choices(months, Month), label="Месяцы", initial=months)


class ChoiceYear(forms.Form):
    year = forms.ChoiceField(choices=lambda : int_choices(get_all_years()), label="Выбор года") #, initial=all_years
