from django import forms
from .models import Contact, Resume

class EmailPostForm(forms.Form):
    name = forms.CharField(max_length=25)
    email = forms.EmailField()
    to = forms.EmailField()
    comments = forms.CharField(required=False, widget=forms.Textarea)


class ContactForm(forms.Form):
    name = forms.CharField(max_length=25)
    email = forms.EmailField()
    to = forms.EmailField()
    subject = forms.CharField(max_length=250)
    message = forms.CharField(widget=forms.Textarea)


class UploadFileForm(forms.ModelForm):
    class Meta:
        model = Resume
        fields = ['file', 'description']
