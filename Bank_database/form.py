#Imports:
import Bank_database.models as model
from django import forms
from django.conf import settings


class Szamlaform(forms.ModelForm):
    meta = model.Szamla
    fields = [
            "aktualis_osszeg",
            "szamla_tulajdonos",
            "szamla_tipus",
    ]
