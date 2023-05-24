from django import forms

class ContactForm(forms.Form):
    name=forms.CharField(max_length=255)
    email=forms.EmailField()    
    contect=forms.Textarea(widget=forms.Textarea)