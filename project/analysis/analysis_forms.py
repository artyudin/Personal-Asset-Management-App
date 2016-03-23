from django import forms
from analysis.analysis_models import Client, Risk, Investment_policy
from analysis.analysis_choices import *
from analysis.labels import *


class ClientForm(forms.ModelForm):
    age = forms.ChoiceField(choices=AGE, label="Your age:", initial='', widget=forms.Select(), required=True)
    marital_status = forms.ChoiceField(choices=MARITAL_STATUS, label="Your martial status: ", initial='', widget=forms.Select(), required=True)
    income = forms.ChoiceField(choices=INCOME, label="Your income:", initial='', widget=forms.Select(), required=True)
    saving_rate = forms.ChoiceField(choices=SAVING_RATE, label="What's your saving rate:", initial='', widget=forms.Select(), required=True)
    fixed_expenses = forms.ChoiceField(choices=FIXED_EXPENSES, label="How much are your fixed expenses? ", initial='', widget=forms.Select(), required=True)
    federal_tax = forms.ChoiceField(choices=FEDERAL_TAX, label="How much is your federal tax? ", initial='', widget=forms.Select(), required=True)
    state_tax = forms.ChoiceField(choices=STATE_TAX, label="How much is you state tax?", initial='', widget=forms.Select(), required=True)
    # user_id = forms.(widget='HiddenInput')
    class Meta:
        model = Client
        fields = [
            "age",
            "marital_status",
            "income",
            "saving_rate",
            "fixed_expenses",
            "federal_tax",
            "state_tax"
            ]

class RiskForm(forms.ModelForm):
    cash_reserves = forms.ChoiceField(label=cash_reserves, choices=CASH_RESERVES, widget=forms.RadioSelect, required=True)
    time_horizont = forms.ChoiceField(label=time_horizont, choices=TIME_HORIZONT, widget=forms.RadioSelect, required=True)
    market_loss = forms.ChoiceField(label=market_loss, choices=MARKET_LOSS, widget=forms.RadioSelect, required=True)
    investment_experience = forms.ChoiceField(label=investment_experience, choices=INVESTMENT_EXPERIENCE, widget=forms.RadioSelect, required=True)
    investment_return = forms.ChoiceField(label=investment_return, choices=INVESTMENT_RETURN, widget=forms.RadioSelect, required=True)
    # user_id = models.(widget='HiddenInput')
    class Meta:
        model = Risk
        fields = [
            'cash_reserves',
            'time_horizont',
            'market_loss',
            'investment_experience',
            'investment_return',
            ]

class Investment_policyForm(forms.ModelForm):
    time_retirement = forms.ChoiceField(label=time_retirement, choices=TIME_RETIREMENT, widget=forms.RadioSelect, required=True)
    liquidity_needs = forms.ChoiceField(label=liquidity_needs, choices=LIQIDITY_NEEDS, widget=forms.RadioSelect, required=True)
    goal_short = forms.ChoiceField(label=goal_short, choices=GOAL_SHORT, widget=forms.RadioSelect, required=True)
    goal_mid = forms.ChoiceField(label=goal_mid, choices=GOAL_MID, widget=forms.RadioSelect, required=True)
    goal_long = forms.ChoiceField(label=goal_long, choices=GOAL_LONG, widget=forms.RadioSelect, required=True)
    expected_return = forms.DecimalField(label=expected_return)
    expected_inflation = forms.DecimalField(label=expected_inflation)
    # user_id = models(widget='HiddenInput')
    class Meta:
        model = Investment_policy
        fields = [
            'time_retirement',
            'liquidity_needs',
            'goal_short',
            'goal_mid',
            'goal_long',
            'expected_return',
            'expected_inflation',
            ]

