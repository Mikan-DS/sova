import datetime

from django import forms


class WriteMessage(forms.Form):
    content = forms.CharField(widget=forms.TextInput(attrs={'id': 'send_message_input'}))
