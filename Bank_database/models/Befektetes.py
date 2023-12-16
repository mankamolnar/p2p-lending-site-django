from django.db import models
from django.conf import settings
from Bank_database.models import Szamla
from Bank_database.models import Kerelem


class Befektetes(models.Model):
    szamla = models.ForeignKey(Szamla, on_delete=models.CASCADE)
    kerelem = models.ForeignKey(Kerelem, on_delete=models.CASCADE)
    osszeg = models.FloatField()
    torlesztett = models.FloatField()

    def __str__(self):
        return str(self.szamla) + str(self.kerelem)