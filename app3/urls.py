from django import views

from django.urls import path
from django.views.generic import TemplateView
from.import views 

urlpatterns = [
  #path('', TemplateView.as_view(template_name='index.html')),
  #path('contact/', views.contactus, name="contact"),
  path('',views.beauty)
]