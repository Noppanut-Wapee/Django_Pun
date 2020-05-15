from django.shortcuts import render # ดึงมาจาก  template
from django.http import HttpResponse #เขียนเอง
from .models import Customer
from django.contrib.auth.models import User #user
from django.shortcuts import redirect

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

def Register(request):
    if request.method == 'POST':
        data = request.POST.copy()
        frist_name = data.get('frist_name')
        last_name = data.get('last_name')
        email = data.get('email')
        password = data.get('password')

        newuser = User()
        newuser.username = email
        newuser.first_name = frist_name
        newuser.last_name = last_name
        newuser.email = email
        newuser.set_password(password)
        newuser.save()
        return redirect('home-page')

    return render(request,'csmuk/register.html')


