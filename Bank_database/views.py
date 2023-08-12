from django.shortcuts import render ,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
# from Bank_database.form import Loginform

# Create your views here.

def login(request):
    if request.method == "GET":
        context = {
            "userform": AuthenticationForm()
        }
        return render(request,"registration/login.html",context)
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('')
        else:
            messages.info(request, "Invalid Username or Password")
        return redirect('login')

# Create your views here.
def register(request):
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        form.save()
        user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password1'])
        login(request, user)
    return render(request, 'registration/registration.html', {'form': form})

@login_required
def main_logged_webpage(request):
    user = request.user
    context = {"user":user}
    return render(request,"logged_in_main_webpage.html",context)