from django import forms
from .models import *

class ModifyEvent(forms.Form):
    title = forms.CharField(max_length=60, label="Название")
    description = forms.CharField(widget=forms.Textarea(attrs={'cols':60, 'rows': 10}), label="Описание")
    event_type = forms.ModelChoiceField(queryset=EventType.objects.all(), label="Тип мероприятия")
    event_level = forms.ModelChoiceField(queryset=EventLevel.objects.all(), label="Уровень мероприятия")
    weorg = forms.BooleanField(required=False, label="Организаторы", initial=True)

class ModifyPlan(forms.Form):
    year = forms.IntegerField(label="Год", initial=2023)
    month = forms.ModelChoiceField(queryset=Month.objects.all(), label="Месяц")
