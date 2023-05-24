from django.shortcuts import render,redirect
from .forms import ContactForm
from django.core.mail import send_mail

from django.template.loader import render_to_string


def index(request):
    
    if request.method=='POST':
        form=ContactForm(request.POST)
        if form.is_valid():
            name=form.cleaned_data['name']
            email=form.cleaned_data['email']
            content=form.cleaned_data['contect']
            
            html=render_to_string('contact/emails/cf.html',{
                'name':name,
                'email':email,
                'content':content
            })
            send_mail('the contact form subject','This is the message','padamsavita786@gmail.com',['avinash2019@gmail.com'],html_message=html)
            
            return redirect('index')
    else:
        form=ContactForm()
        
    return render(request,'contact/index.html',{
        'form':form
    })

def cv(request):
    return render(request,'contact/cv.html')

# Create your views here.
