from Bank_database.models import Szamla

def build(user_id):
    context = {
                "szamla":Szamla.objects.filters(szamla_tulajdonos = user_id)
                }
    return context
     