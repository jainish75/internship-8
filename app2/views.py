from http.client import HTTPResponse
from django.conf import settings
from django.shortcuts import redirect, render
from app2.models import log 
from app2.models import contact,appoint_beauty

from app2.models import registration
from django.core.mail import send_mass_mail

from app3.models import main_menu, sub_menu

# Create your views here.

# def Appointments(request):
#     menu = main_menu.objects.all()
#     submenu=sub_menu.objects.all()
#     if request.method =="POST":
#         prod = Appointments()
#         prod.name = request.POST.get('name')
#         prod.email = request.POST.get('email')
#         prod.phone = request.POST.get('phone')
#         prod.desc = request.POST.get('desc')
#         prod.service = request.POST.get('service')
#         prod.date = request.POST.get('date')
#         prod.time = request.POST.get('time')
#         prod.save()
#         return render(request, "Appointments.html",{'menu': menu,'submenu':submenu})
#     else:
#         return render(request, "Appointments.html",{'menu': menu,'submenu':submenu})

def contactform(request):
    menu = main_menu.objects.all()
    submenu=sub_menu.objects.all()
    if request.method =="POST":
        prod = Contact()
        prod.name = request.POST.get('Yourname')
        prod.email = request.POST.get('YourEmail')
        prod.subject = request.POST.get('Subject')
        prod.msg = request.POST.get('Message')
        prod.save()
        msg="Thank you for contacting us.Your data has been submitted, we will contact you!!"
        message1=(prod.Subject,prod.Message,'jainishsatani411@gmail.com',['jainishsatani411@gmail.com'])
        message2=('confirmation',msg,'jainishsatani411@gmail.com',[prod.YourEmail])
        # send_mass_mail((message1,message2),fail_silently=False)
        #return HTTPResponse("Your data has been submitted")
        return render(request, "contact.html")
    else:
         return render(request,'contact.html')

def login(request):
    if request.method =="POST":
        prod = log()
        prod.uname = request.POST.get('uname')
        prod.Password = request.POST.get('Password')
        prod.save()
        return render(request, "login.html")
    else:
        return render(request, "login.html")

def Registration(request):
    if request.method =="POST":
        prod = registration()
        prod.uname = request.POST.get('uname')
        prod.Email = request.POST.get('Email')
        prod.Password = request.POST.get('Password')
        prod.RPassword = request.POST.get('RPassword')
        prod.save()
        return render(request, "registration.html")
    else:
        return render(request, "registration.html")

def Appoint(request):
    if request.method == "POST":
        prod = appoint_beauty()
        prod.name = request.POST.get('name')
        prod.email = request.POST.get('email')
        prod.phone = request.POST.get('phone')
        prod.desc = request.POST.get('desc')
        prod.service = request.POST.get('service')
        prod.date = request.POST.get('date')
        prod.time = request.POST.get('time')
        # info = Appoint(name=name,  email=email, phone=phone, desc=desc, service=service, date=date, time=time)
        prod.save()
        return render(request, "appointments.html")
    else:
        return render(request,'appointments.html')

# def appoint(request):
#     if request.method == "POST":
#         name = request.POST.get('name')
#         email = request.POST.get('email')
#         phone = request.POST.get('phone')
#         desc = request.POST.get('desc')
#         service = request.POST.get('service')
#         date = request.POST.get('date')
#         time = request.POST.get('time')
#         info = Appoint(name=name,  email=email, phone=phone, desc=desc, service=service, date=date, time=time)
#         info.save()
#     return render(request,'beauty.html')


# def contactform(request):
#     if request.method == "POST":
#         name = request.POST.get('name')
#         email = request.POST.get('email')
#         subject = request.POST.get('subject')
#         msg = request.POST.get('msg')
#         cform = Contact(name=name, email=email, subject=subject, msg=msg)
#         cform.save()
#     return render(request,'contact.html')

def contact(request):
    return render(request,'contact.html')