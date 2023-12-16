from Bank_database.decorators import is_investor
from django.shortcuts import render
from Bank_database.models import Szamla , Befektetes

from Bank_database.views.builder import context_builder

@is_investor
def my_investments(request):
    user = request.user
    account = Szamla.objects.get(szamla_tulajdonos = user)
    invesments = Befektetes.objects.filter(szamla = account)
    context = context_builder.build(user.id)
    context["investments"] = invesments

    return render(request, "my_investments.html", context)