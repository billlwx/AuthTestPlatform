#! /usr/bin/env python
# _*_ coding: utf-8 _*_
# __author__ = 'bill'
# create on 2019/4/18
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

import product
from product.models import Product

@login_required
def product_manage (request):
    uesrname = request.session.get('user', '')
    product_list = Product.objects.all()
    return render(request, "product_manage.html", {"user":uesrname, "products":product_list})