from typing import OrderedDict
from xmlrpc.client import MAXINT

from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.http import HttpResponse, BadHeaderError
from .models import *
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.views.decorators.csrf import *
from .forms import *

# Create your views here.



@csrf_exempt
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password']
        password2 = request.POST['confirm']
        form = Logreg(request.POST)
        if password1 == password2:
           if log.objects.filter(username=username).exists():
                  print('Username are already used')
                  return redirect('/register/')
           elif log.objects.filter(email=email).exists():
                 print('Email invalid')
                 return redirect('/register/')
           else:
                 form.save()
                 print('user created')

        else:
            print('password not matching...')
            return redirect('/register/')
        return redirect('/register/')
    else:
        return render(request, 'register.html')


def reg(request):
    return render(request, 'register.html')


def user(request):
    s = log.objects.last()
    # l = log.objects.get(id)
    return render(request, 'user.html', {'s':s})

def contact_view(request):
    if request.method == 'GET':
        form = ContactForm()
    elif request.method == 'POST':
        # если метод POST, проверим форму и отправим письмо
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            try:
                send_mail(f'{subject} от {from_email}', message,
                          'dauletkyzy.gulzhan@gmail.com',
                          ['200103211@stu.sdu.edu.kz'], fail_silently=False)
            except BadHeaderError:
                return HttpResponse('Ошибка в теме письма.')
                return redirect('success')

    else:
        return HttpResponse('Неверный запрос.')
    return render(request, "sendmessage.html", {'form': form})


def success_view(request):
    return HttpResponse('Приняли! Спасибо за вашу заявку.')