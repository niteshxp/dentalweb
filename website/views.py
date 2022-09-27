# import email
# from turtle import setundobuffer
# from unicodedata import name
from django.shortcuts import render
from django.core.mail import send_mail
# Create your views here.

def home(request):
    return render(request, 'home.html', {})

def contact(request):
    if request.method=="POST":
        # do stuff
        message_name = request.POST['message-name']
        message_email = request.POST['message-email']
        message = request.POST['message']

        #send email
        send_mail (
            message_name, #subject
            message, #message
            message_email, #from email
            ['niteshpatel8852@gmail.com'], # to email
            fail_silently=False,
        )

        return render(request, 'contact.html', {'message_name': message_name})

    else:
        # return the page
        return render(request, 'contact.html', {})
 