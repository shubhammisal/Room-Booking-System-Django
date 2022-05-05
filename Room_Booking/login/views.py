from django.shortcuts import render,redirect
from django.contrib.auth import login as A_login
from django.contrib.auth.forms import AuthenticationForm 
from django.contrib.auth import authenticate
from django.contrib import messages
from django.contrib.auth import logout as A_logout

def login(request):
    if request.method == "POST":
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                A_login(request,user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("home")
            else:
                messages.error(request,"Invalid username or password.")
            request.session['username'] = username
    form = AuthenticationForm()
    return render(request=request, template_name="login/login.html", context={"login_form":form})

def logout(request):
    del request.session['name']
    A_logout(request)
    messages.info(request, "You have successfully logged out.") 
    return redirect("login")