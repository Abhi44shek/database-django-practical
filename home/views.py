from django.shortcuts import render

# Create your views here.

from .models import *
def homeview(request):
    newslist = News.objects.all() # SELECT * from news
    catlist = Category.objects.all()
    ctx = {
        'newslist':newslist,
        'categories':catlist,
    }
    return render(request,'home.html', 
                context= ctx)