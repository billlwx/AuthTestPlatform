# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

import sys
reload(sys)
sys.setdefaultencoding('utf8')

# Create your models here.

class Product(models.Model):
    productname = models.CharField('产品名称', max_length=64)
    productdesc = models.CharField('产品描述', max_length=200)
    producter = models.CharField('产品负责人', max_length=200)
    create_time = models.DateTimeField('创建时间', auto_now=True)

    class Meta:
        verbose_name = '产品管理'
        verbose_name_plural = '产品管理'

    def __str__(self):
        return self.productname