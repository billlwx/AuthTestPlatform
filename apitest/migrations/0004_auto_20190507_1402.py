# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2019-05-07 06:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_auto_20190507_1402'),
        ('apitest', '0003_apis'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='apitest',
            options={'verbose_name': '\u6d41\u7a0b\u573a\u666f\u63a5\u53e3', 'verbose_name_plural': '\u6d41\u7a0b\u573a\u666f\u63a5\u53e3'},
        ),
        migrations.AddField(
            model_name='apis',
            name='apiresponse',
            field=models.CharField(max_length=5000, null=True, verbose_name='\u54cd\u5e94\u6570\u636e'),
        ),
        migrations.AddField(
            model_name='apis',
            name='apitester',
            field=models.CharField(max_length=16, null=True, verbose_name='\u6d4b\u8bd5\u8d1f\u8d23\u4eba'),
        ),
        migrations.AddField(
            model_name='apistep',
            name='apiresponse',
            field=models.CharField(max_length=5000, null=True, verbose_name='\u54cd\u5e94\u6570\u636e'),
        ),
        migrations.AddField(
            model_name='apitest',
            name='Product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='product.Product'),
        ),
        migrations.AddField(
            model_name='apitest',
            name='apitestdesc',
            field=models.CharField(max_length=64, null=True, verbose_name='\u63cf\u8ff0'),
        ),
        migrations.AlterField(
            model_name='apis',
            name='apimethod',
            field=models.CharField(choices=[('get', 'get'), ('post', 'post'), ('put', 'put'), ('delete', 'delete'), ('patch', 'patch')], default='get', max_length=200, null=True, verbose_name='\u8bf7\u6c42\u65b9\u6cd5'),
        ),
        migrations.AlterField(
            model_name='apis',
            name='apiparamvalue',
            field=models.CharField(max_length=800, verbose_name='\u8bf7\u6c42\u53c2\u6570\u548c\u503c'),
        ),
        migrations.AlterField(
            model_name='apistep',
            name='apimethod',
            field=models.CharField(choices=[('get', 'get'), ('post', 'post'), ('put', 'put'), ('delete', 'delete'), ('patch', 'patch')], default='get', max_length=200, null=True, verbose_name='\u8bf7\u6c42\u65b9\u6cd5'),
        ),
        migrations.AlterField(
            model_name='apistep',
            name='apiparamvalue',
            field=models.CharField(max_length=800, verbose_name='\u8bf7\u6c42\u53c2\u6570\u548c\u503c'),
        ),
        migrations.AlterField(
            model_name='apistep',
            name='apistep',
            field=models.CharField(max_length=100, null=True, verbose_name='\u6d4b\u8bd5\u6b65\u805a'),
        ),
        migrations.AlterField(
            model_name='apitest',
            name='apitester',
            field=models.CharField(max_length=16, verbose_name='\u6d4b\u8bd5\u8d1f\u8d23\u4eba'),
        ),
    ]
