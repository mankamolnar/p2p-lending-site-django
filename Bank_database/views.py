from django.shortcuts import render ,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from Bank_database.form import Szamlaform , AddToBalanceForm
from Bank_database.models import Szamla
# from Bank_database.form import Loginform


# Create your views here.
def main(request):
    if request.user.is_authenticated:
        user = request.user
        print(user)
        szamla = Szamla.objects.get(szamla_tulajdonos=user.id)# Model/Helyi
        context = {"user":user,"szamla":szamla}
        return render(request,"logged_in_main_webpage.html",context)
    else:
        return render(request, "index.html", {})


def logged(request):
    if request.method == "GET":
        context = {
            "userform": AuthenticationForm()
        }
        return render(request,"registration/login.html",context)
    if request.method == "POST":
        print("correct")
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
        user_datas = form.save()
        szamla = Szamla(aktualis_osszeg=0,szamla_tulajdonos=user_datas,szamla_tipus=request.POST['account_type'])
        szamla.save()
        user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password1'])
        login(request,user)
        return redirect("main_page")
    else:
        return render(request, 'registration/registration.html', {'form': form})
    

#Functions

def add_currency_to_account(request):
    if request.method == "GET":
        currency = AddToBalanceForm()
        context = {"added_currency": currency}
        return render(request,"add_to_balance.html",context)
    if request.method == "POST":
        user = request.user.id
        account_data = Szamla.objects.get(szamla_tulajdonos = user)
        account_data.aktualis_osszeg = request.POST["osszeg"]
        account_data.save()
        context = {}
        return redirect("main_page")


