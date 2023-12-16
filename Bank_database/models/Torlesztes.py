from django.db import models
from django.conf import settings
from Bank_database.models import Szamla
from Bank_database.models import Kerelem



    


class Torlesztes(models.Model):
    szamla = models.ForeignKey(Szamla, on_delete=models.CASCADE)
    kerelem = models.ForeignKey(Kerelem,on_delete=models.CASCADE)
    osszeg = models.FloatField()


    def __str__(self):
        return str(self.kerelem)