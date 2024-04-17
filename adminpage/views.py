from django.shortcuts import render,redirect
from accounts import views
from userpage.models import *
# from django.contrib import messages
from django.contrib.auth.decorators import login_required



# Create your views here.
@login_required
def adminpage(request):
    return render(request,'admin/homepage.html')

@login_required
def postview(request):
    products = Product.objects.all()
    context={
        'products': products

    }
    return render(request,'admin/post.html',context)
@login_required
def aboutpage(request):
    return render(request,'admin/aboutpage.html')

@login_required
def servicespage(request):
    return render(request,'admin/servicespage.html')

@login_required
def contactpage(request):
    return render(request,'admin/contactpage.html')