# -*- coding:utf-8 -*-
from .models import NAExtraInfo
from django.forms import ModelForm

class NACustomForm(ModelForm):
    """
    The fields on this form are derived from the NAExtraInfo model in models.py.
    """
    def __init__(self, *args, **kwargs):
        super(NACustomForm, self).__init__(*args, **kwargs)
        self.fields['na_names'].error_messages = {
            "required": u"Por favor ingresa Nombres.",
        }
        self.fields['na_lastname_p'].error_messages = {
            "required": u"Por favor ingresa Apellido Paterno.",
        }
        self.fields['na_lastname_m'].error_messages = {
            "required": u"Por favor ingresa Apellido Materno.",
        }
        self.fields['na_rut'].error_messages = {
            "required": u"Por favor ingresa RUT o Pasaporte.",
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
        fields = ('na_rut','na_names','na_lastname_p','na_lastname_m','na_birth_date','na_phone',)

