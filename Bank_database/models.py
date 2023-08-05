from django.db import models
from django.conf import settings

# Create your models here.
class Szamla(models.Model):
    aktualis_osszeg = models.FloatField()
    szamla_tulajdonos = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,)
    szamla_tipus = models.TextField(max_length=255)


class Kerelem(models.Model):
    osszeg = models.FloatField()
    futamido = models.IntegerField()
    kamat = models.FloatField()
    felvett = models.BooleanField()
    leiras = models.TextField()
    torlesztett = models.FloatField()
    szamla = models.ForeignKey(Szamla, on_delete=models.CASCADE)
# szamla_tipust javitani

class Tranzakcio(models.Model):
    szamla_id = models.ForeignKey(Szamla,on_delete=models.CASCADE)
    datatime = models.DateTimeField()
    osszeg = models.FloatField()
    tranzakcio_fajta = models.CharField(max_length=255)

class Befektetes(models.Model):
    szamla = models.ForeignKey(Szamla, on_delete=models.CASCADE)
    kerelem = models.ForeignKey(Kerelem, on_delete=models.CASCADE)
    osszeg = models.FloatField()
    torlesztett = models.BooleanField()


class Torlesztes(models.Model):
    szamla = models.ForeignKey(Szamla, on_delete=models.CASCADE)
    kerelem = models.ForeignKey(Kerelem,on_delete=models.CASCADE)
    osszeg = models.FloatField()
