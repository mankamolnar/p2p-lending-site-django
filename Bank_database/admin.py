from django.contrib import admin

from Bank_database.models.Torlesztes import Torlesztes
from Bank_database.models.Tranzakcio import Tranzakcio
from Bank_database.models.Kerelem import Kerelem
from Bank_database.models.Befektetes import Befektetes
from Bank_database.models.Szamla import Szamla

admin.site.register(Torlesztes)
admin.site.register(Tranzakcio)
admin.site.register(Kerelem)
admin.site.register(Befektetes)
admin.site.register(Szamla)

# Register your models here.
