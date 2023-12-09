from Bank_database.form import Szamlaform ,Userform ,CustomUserCreationForm
from Bank_database.models import Szamla
from django.contrib.auth import authenticate, login
from django.shortcuts import render,redirect


def register(request):
    #form = UserCreationForm(request.POST or None)
    form = CustomUserCreationForm(request.POST or None)
    if form.is_valid():
        user_datas = form.save()
        szamla = Szamla(aktualis_osszeg=0,szamla_tulajdonos=user_datas,szamla_tipus=request.POST['account_type'])
        szamla.save()
        user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password1'])
        login(request,user)
        return redirect("main_page")
    else:
        return render(request, 'registration/registration.html', {'form': form})