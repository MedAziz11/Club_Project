from django import forms
from .models import Request
from django.contrib.admin import widgets

class DateTimeInput(forms.DateTimeInput):
    input_type = 'datetime-local'

class DateForm(forms.ModelForm):
    date = forms.DateTimeField(input_formats=['%d/%m/%Y %H:%M'])
    class Meta:
        model = Request
        fields = ('date',)
        widgets = {'date' : DateTimeInput()}

    