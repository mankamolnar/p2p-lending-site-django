#Imports:
import models as model
from django import forms
from django.conf import settings

class Loginform(forms.ModelForm):
    class Meta:
        model = settings.AUTH_USER_MODEL
        fields = {
                  "username",
                  "password",
                  }
