from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages

from django.http import HttpResponse


def home(request):
    return HttpResponse("Hello, Django!")


def signup_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken!")
        else:
            user = User.objects.create_user(
                username=username, password=password)
            user.save()
            messages.success(request, "Account created! Please login.")
            return redirect("login")

    return render(request, "auths/signup.html")


def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect("/auth/")  # home
        else:
            messages.error(request, "Invalid credentials!")

    return render(request, "auths/login.html")


def logout_view(request):
    logout(request)
    return redirect("login")
