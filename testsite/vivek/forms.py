from django import forms

class NameForm(forms.Form):
      hostname = forms.CharField(label='host',max_length=20)
      package = forms.CharField(label='packet',max_length=100)
