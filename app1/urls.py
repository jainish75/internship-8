from django.urls import path
from . import views

urlpatterns = [


        path('', views.beauty, name="beauty"),
        # path('drop/', views.drop, name="drop"),
        # path('testimonials/',views.testimonials,name=" testimonials"),
        path('about/',views.about,name="about"),
        path('service/',views.service, name="service"),

        
        
]