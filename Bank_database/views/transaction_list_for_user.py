from django.shortcuts import render
from Bank_database.models import Szamla,Tranzakcio

def transaction_list_for_user(request):
    active_user = request.user
    user_account = Szamla.objects.get(szamla_tulajdonos = active_user)
    transactions_of_users = Tranzakcio.objects.filter(szamla_id = user_account)
    context = {"list_items": transactions_of_users}
    return render(request,"transaction_list.html",context)