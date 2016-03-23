from django import forms
from django.contrib.auth.models import User
from portfolio.models import Portfolio, Asset


class PortfolioForm(forms.ModelForm):
    class Meta:
        model = Portfolio
        fields = [
            'portfolio_name',
            ]

class AssetForm(forms.ModelForm):
    class Meta:
        model = Asset
        fields = [
            'quantity',
            'cost_basis',
            ]
     