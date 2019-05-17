# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import render

# Create your views here.
# web用例管理
from webtest.models import Webcase, Webcasestep


@login_required
def webcase_manage(request):
    webcase_list = Webcase.objects.all()
    username = request.session.get('user', '')  # 读取浏览器登录session
    return render(request, "webcase_manage.html",
                  {"user": username, "webcases": webcase_list})


# web用例测试步聚
@login_required
def webcasestep_manage(request):
    username = request.session.get('user', '')
    # webcaseid = request.GET.get('webcase.id', None)
    # webcase = Webcase.objects.get(id=webcaseid)
    webcasestep_list = Webcasestep.objects.all()
    # print webcasestep_list
    return render(request, "webcasestep_manage.html",
                  {"user": username,  "webcasesteps": webcasestep_list})