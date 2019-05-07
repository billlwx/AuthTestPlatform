# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
from apitest.models import Apitest, Apistep, Apis

@login_required
def apitest_manage(request):
    apitest_list = Apitest.objects.all()
    uesrname = request.session.get('user', '')
    return render(request, "api_manage.html", {"user": uesrname, "apitests": apitest_list})

@login_required
def apistep_manage(request):
    apistep_list = Apistep.objects.all()
    uesrname = request.session.get('user', '')
    return render(request, "apistep_manage.html", {"user": uesrname, "apisteps": apistep_list})

@login_required
def apis_manage(request):
    apis_list = Apis.objects.all()
    uesrname = request.session.get('user', '')
    return render(request, "apis_manage.html", {"user": uesrname, "apiss": apis_list})