from django import forms

class UsersForm(forms.Form):
    n1 = forms.CharField(label="Value 1", required=False, widget = forms.TextInput(attrs={'class': 'form-control'}))
    n2 = forms.CharField(label="Value 2", widget = forms.TextInput(attrs={'class': 'form-control'}))