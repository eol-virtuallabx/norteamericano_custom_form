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

def validate_rut(request, rut):
    try:
        if not request.method == 'GET':
            log.error('Wrong Method')
            return HttpResponseNotFound()
        return JsonResponse({'exists_rut': rut_exists(rut)})
    except Exception as e:
        log.error(str(e))
        return HttpResponseBadRequest(u'Ha ocurrido un error')

def rut_exists(na_rut):
    """
        Verify if na_rut exists in NAExtraInfo model
    """
    rut = na_rut.upper()
    if na_rut[0] != 'P':
        aux_rut = na_rut[:-1]
        rut_dv = na_rut[-1].upper()
        rut = "{}-{}".format(aux_rut, rut_dv)
    return NAExtraInfo.objects.filter(na_rut=rut).exists()
