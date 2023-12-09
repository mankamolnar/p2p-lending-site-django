from django.shortcuts import get_object_or_404
from django.shortcuts import render
from Bank_database.models import Szamla

def main(request):

    if request.user.is_authenticated:
        user = request.user
        szamla = get_object_or_404(Szamla,szamla_tulajdonos=user.id)# Model/Helyi
        context = {"user":user,"szamla":szamla}
        return render(request,"logged_in_main_webpage.html",context)
    else:
        return render(request, "index.html", {})