from django.contrib.auth.forms import AuthenticationForm
from django import forms
from django.core.validators import RegexValidator


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))

class ChangeUser(forms.Form):
    number = forms.CharField(max_length=15, validators=[RegexValidator(regex=r'^((\+(7|8))?)(\d{10})$', message="Разрешенно вводить только российские номера в формате +89999999999 без прообелов.")])
    email = forms.EmailField()
    image = forms.ImageField(required=False)
