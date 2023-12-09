from django.db import models
from django.conf import settings

# Create your models here.
class Szamla(models.Model):
    aktualis_osszeg = models.FloatField()
    szamla_tulajdonos = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,)
    szamla_tipus = models.TextField(max_length=255)


    # A login form felhsználhatja a __str__ függvényt nem lehet beloggolni ezzel 
    def __str__(self) -> str:
       return "Account of {0}".format(self.szamla_tulajdonos)
    

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

#    def __str__(self):
#        return str(self.leiras)

    

# szamla_tipust javitani

class Tranzakcio(models.Model):
    szamla_id = models.ForeignKey(Szamla,on_delete=models.CASCADE)
    datatime = models.DateTimeField(auto_now_add=True , null=True, blank=True) #
    osszeg = models.FloatField()
    tranzakcio_fajta = models.CharField(max_length=255)

#    def __str__(self) -> str:
#        return str(self.szamla_id)

class Befektetes(models.Model):
    szamla = models.ForeignKey(Szamla, on_delete=models.CASCADE)
    kerelem = models.ForeignKey(Kerelem, on_delete=models.CASCADE)
    osszeg = models.FloatField()
    torlesztett = models.FloatField()

#    def __str__(self):
#        return str(self.szamla) + str(self.kerelem)
    


class Torlesztes(models.Model):
    szamla = models.ForeignKey(Szamla, on_delete=models.CASCADE)
    kerelem = models.ForeignKey(Kerelem,on_delete=models.CASCADE)
    osszeg = models.FloatField()


#    def __str__(self):
#        return str(self.kerelem)