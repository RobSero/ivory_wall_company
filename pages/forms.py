from django import forms

class MessageForm(forms.Form):
  name = forms.CharField(min_length= 1)
  mobile = forms.IntegerField(min_value=10)
  email = forms.EmailField(required=True)
  message = forms.CharField(max_length=400, min_length= 15)