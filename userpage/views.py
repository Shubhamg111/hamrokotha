from django.shortcuts import render
from .forms import *
from django.shortcuts import render,redirect
# from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# from .models import *
# from . forms import *

# Create your views here.
@login_required
def userpage(request):
    return render(request,"userpage/homepage.html")

@login_required
def uploadpost(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('postlist')
    else:
        form = ProductForm()
    return render(request,"userpage/uploadpost.html",{'form': form})

@login_required
def postlist(request):
    # return render(request,'userpage/postlist.html')

    products = Product.objects.all()
    context={
        'products': products

    }
    return render(request, 'userpage/postlist.html',context)

@login_required
def aboutpage(request):
    return render(request,'userpage/aboutpage.html')

@login_required
def servicespage(request):
    return render(request,'userpage/servicespage.html')

@login_required
def contactpage(request):
    return render(request,'userpage/contactpage.html')