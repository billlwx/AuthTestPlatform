#! /usr/bin/env python
# _*_ coding: utf-8 _*_
# __author__ = 'bill'
# create on 2019/4/23
from django.contrib import auth
from django.http import HttpResponseRedirect
from django.shortcuts import render


def login(request):
    if request.POST:
        userid = request.POST.get('user_id', "")
        password = request.POST.get('password', "")
        user = auth.authenticate(username=userid, password=password)
        if user is not None and user.is_active:
            auth.login(request, user)
            request.session['user'] = userid
            response = HttpResponseRedirect('/apis_manage/')
            return response
        else:
            return render(request, 'login.html', {'error':'userid or password error'})

    return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return render(request,'login.html')