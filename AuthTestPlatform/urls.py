"""AuthTestPlatform URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from AuthTestPlatform import loginview
from apitest import views
from product import proviews
from set import setviews

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^home/', loginview.home),
    url(r'^product_manage/', proviews.product_manage),
    url(r'^apistep_manage/', views.apistep_manage),
    url(r'^apitest_manage/', views.apitest_manage),
    url(r'^apis_manage/', views.apis_manage),
    url(r'^login/', loginview.login),
    url(r'^logout/', loginview.logout),
    url(r'^set_manage/', setviews.set_user),
]
