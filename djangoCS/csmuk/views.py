from django.shortcuts import render # ดึงมาจาก  template
from django.http import HttpResponse #เขียนเอง

def HomePage(request):
    #return HttpResponse('<h1> Hello World Pun</h1>')
    return render(request,'csmuk/home.html')
# Create your views here.