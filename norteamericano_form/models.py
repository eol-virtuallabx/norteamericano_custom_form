# -*- coding:utf-8 -*-
from django.conf import settings
from django.db import models
# ./manage.py lms --settings=production makemigrations custom_reg_form
# ./manage.py lms --settings=production migrate
# Backwards compatible settings.AUTH_USER_MODEL
USER_MODEL = getattr(settings, 'AUTH_USER_MODEL', 'auth.User')


class NAExtraInfo(models.Model):
    """
    This model contains extra fields that will be saved when a user registers.
    The form that wraps this model is in the forms.py file.
    """

    user = models.OneToOneField(USER_MODEL, null=True,on_delete=models.DO_NOTHING,)
    na_firstname = models.CharField(verbose_name=u'Nombres',max_length=100)
    na_lastname = models.CharField(verbose_name=u'Apellidos',max_length=100)
    na_rut = models.CharField(verbose_name=u'RUT',max_length=12)
    na_birth_date = models.CharField(verbose_name=u'Fecha Nacimiento',max_length=10,help_text=u'Formato DD/MM/AAAA')
    na_phone = models.CharField(verbose_name=u'Teléfono',max_length=30)
