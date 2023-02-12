from django import forms

from portfolio.models import *
from users.models import Student


class AddStudent(forms.Form):
    student = forms.ModelChoiceField(queryset=Student.objects.all(), label="Студент")
    event_role = forms.ModelChoiceField(queryset=EventRole.objects.all(), initial=1, label="Роль")

class AddDocument(forms.Form):
    activity = forms.ModelChoiceField(queryset=Activity.objects.none(), label="Активность")
    document_type = forms.ModelChoiceField(queryset=DocumentType.objects.all(), label="Тип документа")
    achievement = forms.ModelChoiceField(queryset=Achievement.objects.all(), label="Достижение")
    image = forms.ImageField(label="Скан")
