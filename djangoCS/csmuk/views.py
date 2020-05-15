from django.shortcuts import render # ดึงมาจาก  template
from django.http import HttpResponse #เขียนเอง
from .models import Customer

def HomePage(request):
    #return HttpResponse('<h1> Hello World Pun</h1>')
    return render(request,'csmuk/home.html')
# Create your views here.


def AboutPage(request):
    return render(request,'csmuk/about.html')

def ContactUs(request):
    return render(request,'csmuk/contactus.html')

def Showcustomer(request):
    customer_all = Customer.objects.all() #ดึงค่าจาก database ทั้งหมด
    context = {'customer_all':customer_all}
    return render(request,'csmuk/showcustomer.html', context)