from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from Bank_database.form import  LendMoneyForm
from Bank_database.models import Szamla

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