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
from .views import CollectionSzList, CollectionShList, CollectionDetailData, CollectionData, CustomComand

urlpatterns = [
    url(r'^collectionSzList', CollectionSzList.as_view(), name='collectionSzList'),
    url(r'^collectionShList', CollectionShList.as_view(), name='collectionShList'),
    url(r'^collectionDetailData', CollectionDetailData.as_view(), name='collectionDetailData'),
    url(r'^collectionData', CollectionData.as_view(), name='collectionData'),
    url(r'^customcomand', CustomComand.as_view(), name='customComand'),
]
