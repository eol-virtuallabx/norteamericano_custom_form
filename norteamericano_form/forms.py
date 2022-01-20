# -*- coding:utf-8 -*-
from .models import NAExtraInfo
from django.forms import ModelForm

class NACustomForm(ModelForm):
    """
    The fields on this form are derived from the NAExtraInfo model in models.py.
    """
    def __init__(self, *args, **kwargs):
        super(NACustomForm, self).__init__(*args, **kwargs)
        self.fields['na_firstname'].error_messages = {
            "required": u"Por favor ingresa Nombres.",
        }
        self.fields['na_lastname'].error_messages = {
            "required": u"Por favor ingresa Apellidos.",
        }
        self.fields['na_rut'].error_messages = {
            "required": u"Por favor ingresa RUT.",
        }
        self.fields['na_birth_date'].error_messages = {
            "required": u"Por favor ingresa Fecha Nacimiento.",
            "invalid":u"Fecha no valida",
        }
        self.fields['na_phone'].error_messages = {
            "required": u"Por favor ingresa Teléfono.",
        }

    class Meta(object):
        model = NAExtraInfo
        fields = ('na_rut','na_firstname','na_lastname','na_birth_date','na_phone',)

