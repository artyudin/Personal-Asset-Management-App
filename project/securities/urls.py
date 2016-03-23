from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^create$', views.AddView.as_view(), name="create"),
    url(r'^list_asset/(?P<id>[A-Za-z0-9-]+)$', views.ListAsset.as_view(), name="list_asset"),
    url(r'^list_stock$', views.StocksListView.as_view(), name="list_stock"),
    url(r'^list_etf$', views.ETFListView.as_view(), name="list_etf"),
    url(r'^list_bond$', views.BondsListView.as_view(), name="list_bond"),
    url(r'^stock_detail/(?P<symbol>[A-Za-z0-9-]+)$', views.StockDetail.as_view(), name='stock_detail'),
    url(r'^bond_detail/(?P<symbol>[A-Za-z0-9-]+)$', views.BondDetail.as_view(), name='bond_detail'),
    url(r'^etf_detail/(?P<symbol>[A-Za-z0-9-]+)$', views.ETFDetail.as_view(), name='etf_detail'),
    url(r'^delete/(?P<id>[A-Za-z0-9-]+)$', views.DeleteAsset.as_view(), name='delete'),
    ]