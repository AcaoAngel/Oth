from django import forms

class Contact_form(forms.Form):

    name=forms.CharField(label='Name', required=True, max_length=20)
    subject=forms.CharField(label="Subject", required=True, max_length=35)
    email=forms.EmailField(label="Email", required=True, max_length=60)
    content=forms.CharField(label="Content", widget=forms.Textarea)
    # a = forms.ImageField()
    # file=forms.FileField()

