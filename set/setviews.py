# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.shortcuts import render

# Create your views here.

#用户管理
def set_user(request):
    user_list = User.objects.all()
    username = request.session.get('user','')
    return render(request, "set_user.html", {"user": username,"users": user_list})

