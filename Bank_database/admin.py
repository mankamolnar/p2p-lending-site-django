from django.contrib import admin

import Bank_database.models as models

admin.site.register(models.Torlesztes)
admin.site.register(models.Tranzakcio)
admin.site.register(models.Kerelem)
admin.site.register(models.Befektetes)
admin.site.register(models.Szamla)

# Register your models here.
