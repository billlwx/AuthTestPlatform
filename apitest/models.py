# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

import sys
reload(sys)
sys.setdefaultencoding('utf8')
# Create your models here.

class Apitest(models.Model):
    # Product = models.ForeignKey('product.Product', on_delete=models.CASCADE, null=True)
    apitestname = models.CharField('流程接口名称', max_length=64)
    # apitestdesc = models.CharField('描述', max_length=64, null=True)
    apitester = models.CharField('执行人', max_length=16)
    apitestresult = models.BooleanField('测试结果')
    create_time = models.DateTimeField('创建时间', auto_now=True)

    def __str__(self):
        return self.apitestname

class Apistep(models.Model):
    Apitest = models.ForeignKey(Apitest, on_delete= models.CASCADE,)
    apistep = models.CharField('测试步骤',max_length=100,null=True)
    apiname = models.CharField('接口名称', max_length=100)
    apiurl = models.CharField('url地址', max_length=200)
    apiparamvalue = models.CharField('请求参数和值', max_length=16)
    # REQUEST_METHOD = (('get', 'get'), ('post', 'post'), ('put', 'put'))
    # apimethod = models.CharField(verbose_name='请求方法', choices=REQUEST_METHOD,default= 'get', max_length=200, null=True)
    apimethod = models.CharField('方法',max_length=200)
    apiresult = models.CharField('预期结果',max_length=200)
    apistatus = models.BooleanField('是否通过')
    create_time = models.DateTimeField('创建时间', auto_now=True)

    def __str__(self):
        return self.apiname
