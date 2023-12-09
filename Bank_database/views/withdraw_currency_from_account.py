
from django.shortcuts import redirect
from Bank_database.models import Szamla
from Bank_database.form import WidthdrawForm
from django.shortcuts import render
from Bank_database.models import Tranzakcio
from Bank_database.views.main import main


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