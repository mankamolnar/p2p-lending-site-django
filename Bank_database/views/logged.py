from Bank_database.form import Userform
from django.shortcuts import render

def logged(request):
    if request.method == "GET":
        context = {
            "form": Userform(),
        }
        return render(request,"registration/login.html",context)