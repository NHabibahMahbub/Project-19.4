from django.shortcuts import render
from platforms.models import Platform
from django.http import HttpResponse
from django.shortcuts import render, redirect
from platforms import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required(login_url='login')
def home(request):
    platform = Platform.objects.all()

    return render(request, 'home.html', {
        "platform": platform
    })


def signup(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        if not (username and email and password1 and password2):
            # return HttpResponse("Please fill in all the fields")
            return redirect("signup")
        if password1 != password2:
            # return HttpResponse("Password didn't matched!")
            return redirect("signup")

        else:
            my_user = User.objects.create_user(username, email, password1)
            my_user.save()
            return redirect("home")

    return render(request, 'signup.html')


def loginPage(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('pass')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return redirect('login')
    return render(request, 'login.html')


def logoutPage(request):
    logout(request)
    return redirect('login')


def details(request, p_id):
    platform = Platform.objects.get(pk=p_id)
    return render(request, 'details.html', {
        "platform": platform
    })
