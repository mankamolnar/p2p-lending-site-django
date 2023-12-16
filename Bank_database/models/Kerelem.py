from django.db import models
from django.conf import settings
from Bank_database.models import Szamla


class Kerelem(models.Model):
    osszeg = models.FloatField()
    futamido = models.IntegerField()
    kamat = models.FloatField()
    leiras = models.TextField()
    #Lender Data's: (Who gives money):
    felvett = models.BooleanField(default=False)
    szamla = models.ForeignKey(Szamla, on_delete=models.CASCADE)
    #Invester's Data's: (Takes money):
    torlesztett =  models.BooleanField(default=False)

    def __str__(self):
        return str(self.leiras)