from django.shortcuts import redirect
from django.http import Http404
from Bank_database.models import Szamla

def is_lender(func):
    def wrapper(*args):
        if args[0].user.is_authenticated:

            if args[0].user.szamla_tipus == "Lender":
                return func(*args)
            else:
                raise Http404("You are not a Lender")
        else:
            return redirect("login/")
    return wrapper
        

def is_investor(func):
    def wrapper(*args):
        if str(args[0].user) != 'AnonymousUser':
            active_user = args[0].user
            user_account = Szamla.objects.get(szamla_tulajdonos = active_user)
            if user_account.szamla_tipus == "Investor":
                return func(*args)
            else:
                raise Http404("You are not an Investor")
        else:
            return redirect("login/")
    return wrapper
