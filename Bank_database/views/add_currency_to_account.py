from Bank_database.views.main import main
from Bank_database.models import Szamla
from Bank_database.form import  TransactionForm
from django.shortcuts import render



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
        return main(request)