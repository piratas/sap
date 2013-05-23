#encoding: utf-8

from django import forms
from django.contrib.localflavor.br.forms import BRCPFField, BRCNPJField, BRZipCodeField, BRStateChoiceField

from .models import GTI

class GTIForm(forms.ModelForm):
    cpf = BRCPFField(label=u'CPF', required=False) 
    estado = BRStateChoiceField(label=u'UF', required=True)

    class Meta:
        model = GTI
