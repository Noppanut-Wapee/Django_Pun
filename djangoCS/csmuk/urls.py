from django.urls import path, include
from .views import HomePage, AboutPage, ContactUs  #ดึงฟังชัน์ใน csmuk มาใช้งาน

urlpatterns = [  
    # localhost:8000/
    path('',HomePage, name='home-page'),
    path('about/',AboutPage, name='about-page'),
    path('contact/',ContactUs, name='contact-page'),

]
