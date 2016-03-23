"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from django.contrib import admin
from users import urls as users_urls
from analysis import urls as analysis_urls
from portfolio import urls as portfolio_urls
from securities import urls as securities_urls

# ***************
# REMOVE
from django.shortcuts import render
def demo(request): return render(request, "index.html")
# *************** 

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^demo' , demo),
    url(r'^', include(users_urls, namespace="users")),
    url(r'^users/', include(users_urls, namespace="users")),
    url(r'^analysis/', include(analysis_urls, namespace='analysis')),
    url(r'^portfolio/', include(portfolio_urls, namespace='portfolio')),
    url(r'^securities/', include(securities_urls, namespace='securities')),
]