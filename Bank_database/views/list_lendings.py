from django.shortcuts import render
from Bank_database.models import  Kerelem
from Bank_database.decorators import is_investor


@is_investor
def list_lendings(request):
        if request.method == "GET":
            context = {
            "kerelmek": Kerelem.objects.filter(felvett=False),
            }
            return render(request, "list_lendings.html", context)
        if request.method == "POST":
            pass