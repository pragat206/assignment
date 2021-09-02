from django import forms


class Main(forms.Form):
    url = forms.CharField(label='URL')
