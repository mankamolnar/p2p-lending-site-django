#Imports:

from django.shortcuts import render,redirect,HttpResponse

#Django implemented model imports:
from django.contrib.auth.models import User,auth

#Django implemented form imports:
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm


#Django error imports:
from django.contrib import messages

#Function imports
from django.contrib.auth import authenticate, login ,logout
from django.contrib.auth.decorators import login_required

#Form imports:
from Bank_database.form import Szamlaform , AddToBalanceForm , Userform ,CustomUserCreationForm , LendMoneyForm

#Model imports:
from Bank_database.models import Szamla, Kerelem

#Error code imports:
from django.core.exceptions import ObjectDoesNotExist

#404 Error handling import:
from django.shortcuts import get_object_or_404

#Login imports:
from django import forms
from django.forms.widgets import TextInput



# Create your views here.
def main(request):
    if request.user.is_authenticated:
        user = request.user
        szamla = get_object_or_404(Szamla,szamla_tulajdonos=user.id)# Model/Helyi
        context = {"user":user,"szamla":szamla}
        return render(request,"logged_in_main_webpage.html",context)


    else:
        return render(request, "index.html", {})

#Login View ()
def logged(request):
    print("Ez az a view")
    if request.method == "GET":
        context = {
            "form": Userform(),
        }
        return render(request,"registration/login.html",context)
    

#Custom login:
'''    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('')
        else:
            messages.info(request, "Invalid Username or Password")
        return redirect('login')'''

#Register function:
def register(request):
    #form = UserCreationForm(request.POST or None)
    form = CustomUserCreationForm(request.POST or None)
    if form.is_valid():
        user_datas = form.save()
        szamla = Szamla(aktualis_osszeg=0,szamla_tulajdonos=user_datas,szamla_tipus=request.POST['account_type'])
        szamla.save()
        user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password1'])
        login(request,user)
        return redirect("main_page")
    else:
        return render(request, 'registration/registration.html', {'form': form})
    

#Functions which used for the pages:
#Nem add hozzá
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
        return main(request)
        #return redirect("main_page")
    
#404 Error handling:
def error_404(request,exception):
    return render(request,"error404.html",{})

@login_required(login_url="/login/")
def list_lendings(request):
        context = {
        "kerelmek": Kerelem.objects.filter(torlesztett=False)
        }
        return render(request, "list_lendings.html", context)
#Kerelem function
def lend_money(request):
    active_user = request.user
    lend_request_form= LendMoneyForm()

    lend_request_form = LendMoneyForm(initial={"szamla":Szamla.objects.get(szamla_tulajdonos = active_user)})
    context = {
        "form":lend_request_form,
    }
    return render(request,"lend_moneysite.html",context)

def my_investments(request):
    return render(request, "my_investments.html", {})
