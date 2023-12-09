#Imports:

from django.shortcuts import render,redirect,HttpResponse

#Logging:
import logging

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
from Bank_database.form import Szamlaform ,Userform ,CustomUserCreationForm , LendMoneyForm, InvestMoneyForm, TransactionForm, WidthdrawForm

#Model imports:
from Bank_database.models import Szamla, Kerelem ,Befektetes ,Tranzakcio

#Error code imports:
from django.core.exceptions import ObjectDoesNotExist

#404 Error handling import:
from django.shortcuts import get_object_or_404

#Login imports:
from django import forms
from django.forms.widgets import TextInput



#Time import:
import time ,datetime


#Logging import:
import logging

#Decorators:
import Bank_database.decorators
from .decorators import is_lender, is_investor
logger = logging.getLogger("View_logger")

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
def add_currency_to_account(request):
    active_user = request.user
    user_account = Szamla.objects.get(szamla_tulajdonos = active_user)
    if request.method == "GET":
        currency_form = TransactionForm(initial={"szamla_id" : user_account, "tranzakcio_fajta":"Befizetés"})
        field1 = currency_form.fields["szamla_id"]
        field3 = currency_form.fields["tranzakcio_fajta"]

        field1.widget = field1.hidden_widget()
        field3.widget = field3.hidden_widget()

        context = {"added_currency": currency_form}
        return render(request,"add_to_balance.html",context)
    
    if request.method == "POST":
        user = request.user.id
        transaction = TransactionForm(request.POST)
        transaction.save()

        account_data = Szamla.objects.get(szamla_tulajdonos = user)
        actual_balance = account_data.aktualis_osszeg
        account_data.aktualis_osszeg = int(request.POST["osszeg"]) + int(actual_balance) #The new actual balance
        account_data.save()
        context = {}
        return main(request) # Instead of redirect to  not load the HTTP again.
    

def withdraw_currency_from_account(request):
    if not request.user.is_authenticated:
        return redirect("login")
    else:
        active_user = request.user
        user_account = Szamla.objects.get(szamla_tulajdonos = active_user)
        print(user_account)
        
        if request.method == "GET":
            withdraw_form = WidthdrawForm()
            context = {"form": withdraw_form}
            return render(request,"withdrawn.html",context)
        elif request.method == "POST":
            
            form_data = WidthdrawForm(request.POST)
            if form_data.is_valid():
                transaction = Tranzakcio()
                data = Tranzakcio(szamla_id = user_account,tranzakcio_fajta = "Kifizetés", osszeg= float(form_data.cleaned_data["osszeg"]))
                data.save()
                return main(request)
                """
                osszeg = form_data.cleaned_data["osszeg"] #Cleaned data validálva van.
                transaction = TransactionForm(initial={"szamla_id" : user_account,"tranzakcio_fajta":"Kifizetés","osszeg": float(osszeg)})
                print(transaction.data)
                if transaction.is_valid(): 
                    print(transaction.data)   
                    transaction.save()
                else:
                    print(transaction.errors.as_data())
                context = {}
            return main(request)
            """


def transaction_list_for_user(request):
    active_user = request.user
    user_account = Szamla.objects.get(szamla_tulajdonos = active_user)
    transactions_of_users = Tranzakcio.objects.filter(szamla_id = user_account)
    context = {"list_items": transactions_of_users}
    return render(request,"transaction_list.html",context)


#404 Error handling:
def error_404(request,exception):
    return render(request,"error404.html",{})


@is_investor
def list_lendings(request):
        if request.method == "GET":
            context = {
            "kerelmek": Kerelem.objects.filter(felvett=False),
            }
            return render(request, "list_lendings.html", context)
        if request.method == "POST":
            pass
#Kerelem function


@is_investor
def my_investments(request):
    return render(request, "my_investments.html", {})

@login_required(login_url="/login/")
def lend_money(request):
    
    if request.method == "POST":
        form = LendMoneyForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,"lend_moneysite_succes_save.html",{})
    else:
        active_user = request.user
        #post or none intial-el
        lend_request_form = LendMoneyForm(initial={"szamla":Szamla.objects.get(szamla_tulajdonos = active_user)})
        field = lend_request_form.fields["szamla"]
        field.widget = field.hidden_widget()
        context = {
            "form":lend_request_form,
        }
        return render(request,"lend_moneysite.html",context)
    
#Invest Money it takes the Lended money and add it to the logged user's account:
@is_investor
def invest_money(request,id):
    #https://stackoverflow.com/questions/48097400/wrapper-got-an-unexpected-keyword-argument-id
    active_user = request.user
    choosen_invest = Kerelem.objects.get(pk=id)
    if request.method == "POST":
        invest_money_form = InvestMoneyForm(request.POST or None)
        active_user_account_data = Szamla.objects.get(szamla_tulajdonos = active_user)
        
        #Have to make a Befeketes form:
        if invest_money_form.is_valid():
            

            # Kerelem Check felvett or not:
            lend_connected_invest = choosen_invest.befektetes_set.all()

            
            #Starter money we count from zero then count all Invest's.
            zero_money = 0
            for lended_money in lend_connected_invest:
                    zero_money += lended_money.osszeg

            if int(invest_money_form.cleaned_data["osszeg"]) +  int(zero_money) <= choosen_invest.osszeg:

                if int(choosen_invest.osszeg - zero_money- invest_money_form.cleaned_data["osszeg"]) <= 0:
                    # Deleteing Lend from the Lender_list:
                    choosen_invest.felvett = True  
                else:
                    choosen_invest.felvett = False
            else:
                return render(request,"error404.html",{})

            


            # Money Transfer from the Lender to the Invester:
            actual_balance = active_user_account_data.aktualis_osszeg
            new_balance = int(actual_balance) + int(invest_money_form.cleaned_data["osszeg"])
            active_user_account_data.aktualis_osszeg = new_balance


            active_user_account_data.save()
            choosen_invest.save()
            invest_money_form.save()

            #Logging Warning test not working print helyett
            #logging.warning(choosen_invest)

            
            context = {"lended_money": choosen_invest.osszeg}
            return redirect("list_lendings")
        else:
            # If the data is not saved
            print("Data save was unsuccesfull")
    else:
        choosen_invester_account = choosen_invest.szamla
        invest_money_form = InvestMoneyForm(initial={"szamla":choosen_invester_account,
                                                     "kerelem":choosen_invest.id,
                                                     "torlesztett": 0,
                                                     })
        
        # Widget cell description létrehoztam a widgetek.
        field1 = invest_money_form.fields["szamla"]
        field2 = invest_money_form.fields["kerelem"]
        field3 = invest_money_form.fields["torlesztett"]

        #A hidden widgettek kellenek.
        field1.widget = field1.hidden_widget()
        field2.widget = field2.hidden_widget()
        field3.widget = field3.hidden_widget()

        context = {"form": invest_money_form,
                   } 
        return render(request,"lending_take_confirmation.html",context)
        
@is_lender
def list_your_taken_money(request):
    pass
    active_user = request.user
    own_investments = Kerelem.objects.get(invester_balance = active_user)
    context = {"investments":own_investments}
    return render(request,"",context)





    



    



