from django import forms
from securities.securities_models import Stock, Bond, ExchangeTradedFund

class StockForm(forms.ModelForm):
	class Meta:
		model = Stock
		fields = ['symbol', 'company_name', 'sector', 'industry', 'market_capitalization']

class BondForm(forms.ModelForm):
	class Meta:
		model = Bond
		fields = ['symbol', 'company_name', 'coupon', 'maturity_date', 'sp_rating', 'moody_rating']


class ExchangeTradedFundForm(forms.ModelForm):
	class Meta:
		model = ExchangeTradedFund
		fields = ['symbol', 'name', 'category', 'fund_family', 'beta', 'alpha', 'r_squared', 'sharpe_ratio']

