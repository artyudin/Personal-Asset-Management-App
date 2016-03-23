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
from django.conf.urls import url
from . import views
urlpatterns = [
    # url(r'^$', views.Index.as_view(), name="index"),
    url(r'^$', views.Index.as_view(), name="dashboard"),
    url(r'^create$', views.CreatePortfolio.as_view(), name="create"),
    url(r'^show_list$', views.ShowPortfolio.as_view(), name="show_list"),
    url(r'^delete/(?P<id>[A-Za-z0-9-]+)$', views.DeletePortfolio.as_view(),
         name='delete'),
    url(r'^update/(?P<id>[A-Za-z0-9-]+)$', views.UpdatePortfolio.as_view(),
         name='update'),
    url(r'^portfolio_detail/(?P<pk>[A-Za-z0-9-]+)$', views.PortfolioDetailView.as_view(), name='portfolio_detail'),
    
]
