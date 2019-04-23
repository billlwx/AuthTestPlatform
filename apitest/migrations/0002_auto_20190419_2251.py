# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2019-04-19 14:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apitest', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='apitest',
            options={},
        ),
        migrations.RemoveField(
            model_name='apitest',
            name='Product',
        ),
        migrations.RemoveField(
            model_name='apitest',
            name='apitestdesc',
        ),
        migrations.AddField(
            model_name='apistep',
            name='apistep',
            field=models.CharField(max_length=100, null=True, verbose_name='\u6d4b\u8bd5\u6b65\u9aa4'),
        ),
        migrations.AlterField(
            model_name='apistep',
            name='apimethod',
            field=models.CharField(max_length=200, verbose_name='\u65b9\u6cd5'),
        ),
        migrations.AlterField(
            model_name='apitest',
            name='apitester',
            field=models.CharField(max_length=16, verbose_name='\u6267\u884c\u4eba'),
        ),
    ]
