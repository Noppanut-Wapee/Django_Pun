from django.shortcuts import render
#from django.http import HttpResponse 


# Create your views here.
def index(request):
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
    
    return render(request,'page1.html',{'a':'Hello page1 Noppanut!!'})

#def page2(request):

 #   return render(request,'page2.html',{'b':'Hello Page2 Noppanut!!'})

def createForm(request):

    return render(request,'createForm.html',{'b':'Hello Page2 Noppanut!!'})

def addBlog(request):
    return render(request,'result.html')

