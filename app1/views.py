from django.shortcuts import render
from app1.models import slide,offerimg,servicename,activ
from app3.models import Detail, main_menu,sub_menu
from django.shortcuts import render
#from .models import Mo_number, event_1, room_C1 , room_C2, room_C3, logo, scroller, blog_0, Navbar, about_us, Hotel_name, address



# Create your views here.w
def beauty(request):
    menu = main_menu.objects.all()
    submenu=sub_menu.objects.all()
    detail = Detail.objects.all()
    sliders=slide.objects.all()
    offerimgs=offerimg.objects.all()
    return render(request, "beauty.html", {'menu': menu,'submenu':submenu, 'detail' :detail, 'sliders':sliders,'offerimgs':offerimgs}) 

def about(request):
    menu = main_menu.objects.all()
    submenu=sub_menu.objects.all()
    offerimgs=offerimg.objects.all()
    activs=activ.objects.all()
    return render(request,"about.html",{'menu':menu,'submenu':submenu,'offerimgs':offerimgs,'activs':activs})

    
def service(request):
    menu = main_menu.objects.all()
    submenu=sub_menu.objects.all()
    offerimgs=offerimg.objects.all()
    servicen=servicename.objects.all()
    return render(request,'service.html',{'menu':menu,'submenu':submenu,'offerimgs':offerimgs,'servicen':servicen})
