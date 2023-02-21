import datetime

from django import forms


class WriteMessage(forms.Form):
    content = forms.CharField(widget=forms.Textarea(
        attrs={
            'id': 'send_message_input',
            "autocomplete": "off"
        }))
