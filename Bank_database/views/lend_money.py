from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from Bank_database.form import  LendMoneyForm
from Bank_database.models import Szamla
from Bank_database.decorators import is_lender


@is_lender
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
        user_account = Szamla.objects.get(szamla_tulajdonos = active_user)
        context = {
            "form":lend_request_form,
            "account": user_account,
        }
        return render(request,"lend_moneysite.html",context)