from django import forms

class SearchVideoForm(forms.Form):
    desc = forms.CharField(label='Title',max_length=100)
    