from django.db import models
from analysis.analysis_choices import *
from users.models import Profile
from django.contrib.auth.models import User


class Client(models.Model):
	age = models.CharField(max_length=25, choices=AGE)
	marital_status = models.CharField(max_length=25, choices=MARITAL_STATUS)
	income = models.CharField(max_length=25, choices=INCOME)
	saving_rate = models.CharField(max_length=25, choices=SAVING_RATE)
	fixed_expenses = models.CharField(max_length=25, choices=FIXED_EXPENSES)
	federal_tax = models.DecimalField(max_digits=10, decimal_places=2, choices=FEDERAL_TAX)
	state_tax = models.DecimalField(max_digits=10, decimal_places=2, choices=STATE_TAX)
	user = models.OneToOneField(User)

class Risk(models.Model):
	cash_reserves = models.IntegerField(choices=CASH_RESERVES)
	time_horizont = models.IntegerField(choices=TIME_HORIZONT)
	market_loss = models.IntegerField(choices=MARKET_LOSS)
	investment_experience = models.IntegerField(choices=INVESTMENT_EXPERIENCE)
	investment_return = models.IntegerField(choices=INVESTMENT_RETURN)
	score = models.IntegerField(default = 0)
	user = models.OneToOneField(User)

class Investment_policy(models.Model):
	time_retirement = models.CharField(max_length=20, choices=TIME_RETIREMENT)
	liquidity_needs = models.CharField(max_length=50, choices=LIQIDITY_NEEDS)
	goal_short = models.CharField(max_length=50, choices=GOAL_SHORT)
	goal_mid = models.CharField(max_length=50, choices=GOAL_MID)
	goal_long = models.CharField(max_length=50, choices=GOAL_LONG)
	expected_return = models.DecimalField(max_digits=3, decimal_places=2)
	expected_inflation = models.DecimalField(max_digits=3, decimal_places=2)
	user = models.OneToOneField(User)
	
	


