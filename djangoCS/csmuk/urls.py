from django.urls import path, include
# from .views import HomePage, AboutPage, ContactUs, Showcustomer  #ดึงฟังชัน์ใน csmuk มาใช้งาน
from .views import * #แบบนี้ไม่ต้องพิมพ์ จะเอามาทั้งหมดเลย
urlpatterns = [  
    # localhost:8000/
    path('',HomePage, name='home-page'),
    path('about/',AboutPage, name='about-page'),
    path('contact/',ContactUs, name='contact-page'),
    path('showcustomer/',Showcustomer, name='customer-page'),
    path('register/',Register, name='register-page'),
]
