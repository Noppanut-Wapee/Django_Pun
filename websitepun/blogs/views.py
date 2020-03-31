from django.shortcuts import render
#from django.http import HttpResponse 


# Create your views here.
def hello(request):
    tags =('น้ำตก','ภูเขา','ทะเล','ตากหมอก','ปีนเขา')
    return render(request,'index.html',
    {
    'name':'บทความท่องเที่ยว',
    'author':'Noppanut',
    'tags': tags
     })
    


