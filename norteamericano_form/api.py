# -*- coding:utf-8 -*-
import logging
from django.conf import settings
from django.db import models
from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.decorators.http import require_http_methods
from .models import NAExtraInfo
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_exempt
from django.contrib.auth.decorators import login_required
from util.json_request import JsonResponse
from django.http.response import HttpResponseBadRequest, HttpResponseForbidden,HttpResponseNotFound

import re
import requests

log = logging.getLogger(__name__)

def validate_rut(request,rut):
    try:
        if not request.method == 'GET':
            return HttpResponseNotFound()
        if rut_exists(rut):
            return JsonResponse({'result': False, 'exists_rut': True})
        
        return JsonResponse({'result':True if result == '100' else False, 'exists_rut': False})
    except Exception as e:
        log.error(str(e))
        return HttpResponseBadRequest(u'Ha ocurrido un error')

def rut_exists(na_rut):
    """
        Verify if na_rut exists in NAExtraInfo model
    """
    aux_rut = na_rut[:-1]
    rut_dv = na_rut[-1].upper()
    rut = re.sub(r'(?<!^)(?=(\d{3})+$)', r'.', aux_rut)
    rut = "{}-{}".format(rut, rut_dv)
    return NAExtraInfo.objects.filter(na_rut=rut).exists()
