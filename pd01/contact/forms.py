from django import forms

class ContactForm(forms.Form):
    name=forms.CharField(
         label="",
         widget=forms.TextInput(attrs={'placeholder': 'Enter your Name','class':'form-control'}),
        max_length=255)
    email=forms.EmailField(
        label="",
        widget=forms.TextInput(attrs={'placeholder': 'Enter your email','class':'form-control'}),

        
    )    
    contect=forms.CharField(
        label="",

        widget=forms.Textarea(attrs={'placeholder':'Enter your message','class':'form-control'}))