from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import SignupForm
from django.contrib import messages





def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS,'New Acoount Created')
            return redirect('login')
        else:
            messages.add_message(request,messages.ERROR,'Failed To Register')
            return render(request, 'accounts/signup.html', {'form': form})

    else:
        form = SignupForm()
    return render(request, 'accounts/signup.html', {'form': form})

# def login_view(request):
#     if request.method == 'POST':
#         form = AuthenticationForm(data=request.POST)
#         if form.is_valid():
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password')
#             user = authenticate(username=username, password=password)
#             if user is not None:
#                 login(request, user)
#                 return redirect('home')  # Redirect to desired page
#     else:
#         form = AuthenticationForm()
#     return render(request, 'accounts/login.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                if user.is_staff:  # Check for admin status
                    messages.add_message(request,messages.SUCCESS,'Admin Login Successfull')
                    return redirect('adminpage')  # Redirect to admin page
                elif not user.is_staff:
                    messages.add_message(request,messages.SUCCESS,'User Login Successfull')
                    return redirect('userpage')  # Redirect to user page
                else:
                    messages.add_message(request,messages.ERROR,'Failed To Login')
                    return render(request, 'accounts/login.html', {'form': form})

                    
                    
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('/')

