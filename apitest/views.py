# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.decorators import login_required
from django.db.models import Count
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

# 测试报告
@login_required
def test_report(request):
    username = request.session.get('user', '')
    apis_list = Apis.objects.all()
    apis_count = Apis.objects.all().count()  #统计接口数
    # sql1 = 'SELECT count(id) FROM apitest_apis WHERE apitest_apis.apistatus=1'
    # sql2 = 'SELECT count(id) FROM apitest_apis WHERE apitest_apis.apistatus=0'
    # apis_fail_count = [row[0] for row in cursor.fetchmany(bb)][0]
    # aa = Apis.objects.get(apistatus=1)
    # print aa
    return render(request, "report.html", {"user": username,"apiss": apis_list,"apiscounts": apis_count}) #把值赋给apiscounts这个变量