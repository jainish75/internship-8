from django.shortcuts import render
from app3.models import Detail, navbar

# Create your views here.
def beauty(request):
    detail =  Detail.objects.all()
    Navbar =  navbar.objects.all()

    return render(request,"beauty.html",{'navbar': Navbar,'detail' : detail,})


from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import main_menu, sub_menu


# Create your views here.


def mainmenu(request):
    menu = main_menu.objects.all()
    submenu=sub_menu.objects.all()
    return render(request, 'menu.html', {'menu': menu,'submenu':submenu})


def mainsave(request):
    if request.method == 'POST':
        mname = request.POST['menu_name']
        mlink = request.POST['mn_link']
        main_menu.objects.create(m_menu_name=mname, m_menu_link=mlink)
        # return HttpResponse("created")
        return redirect('mainmenu')
    else:
        return redirect('mainmenu')


def subsave(request):
    if request.method == 'POST':
        menuid=request.POST['parent']
        sname=request.POST['sub_menu_name']
        slink=request.POST['sub_menu_link']
        sub_menu.objects.create(m_menu_id=menuid,s_menu_name=sname,s_menu_link=slink)
        return redirect('mainmenu')
    else:
        return redirect('mainmenu')

def dynamic_menu(request):
    menu = main_menu.objects.all()
    submenu = sub_menu.objects.all()
    return render(request, 'beauty.html', {'menu': menu, 'submenu': submenu})


# def appoint(request):
#     if request.method == "POST":
#         name = request.POST.get('name')
#         email = request.POST.get('email')
#         phone = request.POST.get('phone')
#         desc = request.POST.get('desc')
#         service = request.POST.get('service')
#         date = request.POST.get('date')
#         time = request.POST.get('time')
#         info = Appoint( email=email, phone=phone, desc=desc, service=service, date=date, time=time)
#         info.save()
#     return render(request,'index.html')