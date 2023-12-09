from Bank_database.decorators import is_investor
from django.shortcuts import render

@is_investor
def my_investments(request):
    return render(request, "my_investments.html", {})