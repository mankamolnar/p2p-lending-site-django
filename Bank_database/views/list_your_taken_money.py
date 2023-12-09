from Bank_database.decorators import is_lender
from Bank_database.models import  Kerelem
from django.shortcuts import render

@is_lender
def list_your_taken_money(request):
    pass
    active_user = request.user
    own_investments = Kerelem.objects.get(invester_balance = active_user)
    context = {"investments":own_investments}
    return render(request,"",context)