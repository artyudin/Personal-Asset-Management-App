from django.conf.urls import url
from . import views
urlpatterns = [
	url(r'^analysis$', views.ClientCreateView.as_view(), name="analysis"),
	url(r'^risk$', views.RiskView.as_view(), name="risk"),
	url(r'^policy$', views.Investment_policyView.as_view(), name="policy"),
	url(r'^beta_analysis/(?P<id>[A-Za-z0-9-]+)$', views.BetaAnalysisView.as_view(), name="beta_analysis"),
	url(r'^report_policy$', views.ReportInvestmentPolicy.as_view(), name="report_policy"),
	url(r'^compare/(?P<id>[A-Za-z0-9-]+)$', views.Compare_with_model.as_view(), name="compare"),
	url(r'^model_portfolio$', views.View_model_portfolio.as_view(), name="model_portfolio"),



	]




