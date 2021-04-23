from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages, auth

# Create your views here.

def login_view(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            # handle login
            if request.POST["email"] and request.POST["password"]:
                try:
                    user = User.objects.get(email = request.POST["email"])
                    auth.login(request, user)
                    if request.POST.get("next"):
                        return redirect(request.POST['next'])
                    return redirect("/")
                except User.DoesNotExist:
                    return render(request, "login.html", { "error" : "User doesn't exist!" })
            else:
                return render(request, "login.html", { "error" : "Empty fields!" })
        else:
            return render(request, "login.html")
    else:
        return redirect("/")

def signup_view(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            username_ = request.POST["username"]
            email_ = request.POST["email"]
            password_ = request.POST["password"]
            password2 = request.POST["password"]
            # handle signup
            if password_ == password2:
                if username_ and email_ and password_:
                    try:
                        user = User.objects.get(email=email_)
                        if user:
                            return render(request, "signup.html", { "error" : "User already exists"})
                    except User.DoesNotExist:
                        User.objects.create_user(
                            username = username_,
                            email = email_,
                            password = password_,
                        )
                        messages.success(request, "SignUp Successful \n Login Here")
                        return redirect(login_view)
                else:
                    return render(request, "signup.html", { "error" : "Empty fields"}) 
            else:
                return render(request, "signup.html", { "error" : "Passwords don't match"})
        else:
            return render(request, "signup.html")
    else:
        return redirect("/")

def logout_view(request):
    auth.logout(request)
    return redirect("/login")
