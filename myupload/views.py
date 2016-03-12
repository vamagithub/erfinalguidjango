# Create your views here.
from django.shortcuts import render
from django.core.mail import EmailMessage
from django.http import HttpResponse

# Create your views here.
from mysite import settings


def Form(request):
    return render(request,"form.html",{})


def Upload(request):
    mail = EmailMessage('subject', 'message', 'email', [settings.EMAIL_HOST_USER])
    for count, x in enumerate(request.FILES.getlist("files")):
        mail.attach(x.name, x.read().decode("utf-8"), x.content_type)    # change ur type in unix system use only x.read()
    mail.send()

    return HttpResponse("Files Sent !")
