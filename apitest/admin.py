# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from apitest.models import Apistep, Apitest, Apis


class ApistepAdmin(admin.TabularInline):
    list_display = ['apiname', 'apiurl', 'apiparamvalue', 'apimethod', 'apiresult', 'apistatus', 'id', 'Apitest']
    model = Apistep
    extra = 1

class ApitestAdmin(admin.ModelAdmin):
    list_display = ['apitestname', 'apitester', 'apitestresult', 'create_time', 'id']
    inlines = [ApistepAdmin]

admin.site.register(Apitest,ApitestAdmin)

class ApisAdmin(admin.TabularInline):
    list_display = ['apiname', 'apiurl', 'apiparamvalue', 'apiresult', 'apiresult', 'create_time', 'id', 'product']
    admin.site.register(Apis)