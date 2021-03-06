"""stock URL Configuration

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
from django.conf.urls import url, include
from .views import HighStock, CustomStock, ShStock, SzStock

urlpatterns = [
    url(r'^highStock', HighStock.as_view(), name='highStock'),
    url(r'^customStock', CustomStock.as_view(), name='customStock'),
    url(r'^shstock', ShStock.as_view(), name='shStock'),
    url(r'^szstock', SzStock.as_view(), name='szStock'),
]
