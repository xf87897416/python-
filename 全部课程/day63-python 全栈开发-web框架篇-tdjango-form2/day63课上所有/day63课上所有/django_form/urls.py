"""django_form URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from app01 import views
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^login.html$', views.login),
    url(r'^login_ajax.html$', views.login_ajax),
    url(r'^index.html$', views.index),
    url(r'^edit_index.html$', views.edit_index),
    url(r'^detail.html$', views.detail),
    url(r'^field.html$', views.field),
    url(r'^widght.html$', views.widght),
    url(r'^db.html$', views.db),
    url(r'^initial.html$', views.initial),
]
