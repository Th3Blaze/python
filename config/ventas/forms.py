from django import forms
from .models import *

class busquedaForm(forms.Form):
    nombre_cliente=forms.CharField(required=False)
    producto_vendido=forms.CharField(required=False)
    pais_cliente=forms.CharField(required=False)