from django.db import models
from django.conf import settings


class Szamla(models.Model):
    aktualis_osszeg = models.FloatField()
    szamla_tulajdonos = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,)
    szamla_tipus = models.TextField(max_length=255)


    # A login form felhsználhatja a __str__ függvényt nem lehet beloggolni ezzel 
    def __str__(self) -> str:
       return "Account of {0}".format(self.szamla_tulajdonos)