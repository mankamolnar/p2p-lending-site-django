#Imports:
import Bank_database.models as model
from django import forms
from django.conf import settings


class Szamlaform(forms.ModelForm):
    class Meta:
        model=model.Szamla
        fields = [
                "aktualis_osszeg",
                "szamla_tulajdonos",
                "szamla_tipus",
        ]

class AddToBalanceForm(forms.Form):
    osszeg = forms.FloatField()