from django.shortcuts import render

# Create your views here.
def homepage(request):
    return render(request,'templates/homepage.html')


def contactpage(request):
    return render(request,'templates/contactpage.html')

def aboutpage(request):
    return render(request,'templates/aboutpage.html')

def servicespage(request):
    return render(request,'templates/servicespage.html')