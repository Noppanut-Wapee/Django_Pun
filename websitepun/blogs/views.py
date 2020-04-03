from django.shortcuts import render
#from django.http import HttpResponse 


# Create your views here.
def hello(request):
    tags =('น้ำตก','ภูเขา','ทะเล','ตากหมอก','ปีนเขา')
    rating = 3
    return render(request,'index.html',
    {
    'name':'บทความท่องเที่ยว',
    'author':'Noppanut',
    'tags': tags,
    'rating':rating
    })
    
def page1(request):
    
    return render(request,'page1.html',{'a':'Hello Noppanut!!'})

