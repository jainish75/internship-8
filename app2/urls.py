from django.urls import path

# from app2.models import contact
from . import views

urlpatterns = [

        path('log/', views.login , name="log"),
        path('contact/',views.contact,name="contact"),
        # path('appointments/', views.Appointments , name="appointments"),
        path('registration/',views.Registration, name="registration"),
        # path('dinning/',views.Dinning, name="dinning"),
        # path('news/',views.News, name="news"),
        path('appoint/',views.Appoint, name="appoint"),
    path('contactform/',views.contactform,name='contactform'),



]