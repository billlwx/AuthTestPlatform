# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from apitest.models import Apis
from product.models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ['productname', 'productdesc', 'producter', 'create_time', 'id']
    admin.site.register(Product)
    # inlines = [ApisAdmin]

class ApisAdmin(admin.TabularInline):
    list_display = ['apiname', 'apiurl', 'apiparamvalue', 'apiresult', 'apiresult', 'create_time', 'id', 'product']
    model = Apis
    extra = 1

class ProductAdmin(admin.ModelAdmin):
    list_display = ['productname', 'productdesc', 'create_time', 'id']
    inlines = [ApisAdmin]