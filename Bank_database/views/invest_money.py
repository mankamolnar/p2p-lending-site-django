from Bank_database.decorators import is_investor
from Bank_database.models import Szamla, Kerelem
from Bank_database.form import InvestMoneyForm
from django.shortcuts import render,redirect

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