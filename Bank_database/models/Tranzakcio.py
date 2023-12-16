from django.db import models
from django.conf import settings
from Bank_database.models import Szamla

class Tranzakcio(models.Model):
    szamla_id = models.ForeignKey(Szamla,on_delete=models.CASCADE)
    datatime = models.DateTimeField(auto_now_add=True , null=True, blank=True) #
    osszeg = models.FloatField()
    tranzakcio_fajta = models.CharField(max_length=255)


    def __str__(self) -> str:
        return self.szamla_id 