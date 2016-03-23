from django.shortcuts import render
from .securities_forms import StockForm
from django.views.generic import View
from portfolio.models import Asset, Portfolio
from securities.securities_models import Stock, Bond, ExchangeTradedFund
from django.http import JsonResponse
from django.contrib.contenttypes.models import ContentType
from decimal import *



class AddView(View):


    def post(self,request):
        # form = self.form_class(data=request.POST)
        data = request.POST
        id_int = int(data.get('choice_asset').split(',')[1])
        content_type = data.get('content_type')
        if content_type =='stock': 
            asset_spec = Stock.objects.get(id=id_int)
        elif content_type == "etf":
            asset_spec = ExchangeTradedFund.objects.get(id=id_int)
        elif content_type =='bond':
            asset_spec = Bond.objects.get(id=id_int)


        content_object = asset_spec
        id_portfolio = int(data.get('id_portfolio'))
        portfolio =Portfolio.objects.get(id=id_portfolio)

        data=request.POST

        asset, created  = Asset.objects.get_or_create(object_id=asset_spec.id, 
            content_type=ContentType.objects.get_for_model(asset_spec),
            portfolio = portfolio
                )
        if created:
            asset.quantity = int(data.get('quantity'))
            asset.cost_basis = data.get('cost_basis')
        else: 
            total_quantity = asset.quantity + int(data.get('quantity'))
            print(total_quantity)
            value_old_assets = Decimal(asset.cost_basis) * asset.quantity
            print(value_old_assets)
            value_new_assets = int(data.get('quantity')) * Decimal(data.get('cost_basis'))
            print(value_new_assets)
            asset.cost_basis = (value_new_assets + value_old_assets) /  total_quantity
            asset.quantity = total_quantity

        asset.save()
        
        
        return JsonResponse({'asset':asset.to_json(0,1)})

class ListAsset(View): 
    def get(self,request,id):
        portfolio =Portfolio.objects.get(id=id)
        # assets = Asset.objects.filter(portfolio=portfolio)
        assets= Asset.objects.raw('''SELECT *, cost_basis * quantity as value 
            FROM portfolio_asset
            WHERE portfolio_asset.portfolio_id = %s ''',(id,))
        # print(assets)
        portfolio_value = 0 
        for asset in assets:
            portfolio_value += asset.value
        
        assets = [ asset.to_json(asset.value,portfolio_value)for asset in assets ]

        # print(assets)
        return JsonResponse({'asset':assets,'portfolio_value':portfolio_value})




class StocksListView(View):
    
    def get(self,request):
        stocks = Stock.objects.all()
        stocks = [stock.to_json() for stock in stocks]
        return JsonResponse({'stocks':stocks, 'content_type':'stock'})

class ETFListView(View):
    
    def get(self,request):
        exchangeTradedFunds = ExchangeTradedFund.objects.all()
        exchangeTradedFunds = [exchangeTradedFund.to_json() for exchangeTradedFund in exchangeTradedFunds]
        return JsonResponse({'exchangeTradedFunds':exchangeTradedFunds, 'content_type':'etf'})

class BondsListView(View):
    
    def get(self,request):
        bonds = Bond.objects.all()
        bonds = [bond.to_json() for bond in bonds]
        return JsonResponse({'bonds':bonds, 'content_type':'bond'})


class StockDetail(View):

    def get(self,request,symbol):
        stock = Stock.objects.get(id=symbol)
        return JsonResponse({'stock':stock.to_json()})


class BondDetail(View):

    def get(self,request,symbol):
        bond = Bond.objects.get(id=symbol)
        return JsonResponse({'bond':bond.to_json()})



class ETFDetail(View):

    def get(self,request,symbol):
        etf = ExchangeTradedFund.objects.get(id=symbol)
        return JsonResponse({'etf':etf.to_json()})



class DeleteAsset(View):
    
    
    def get(self,request,id):
        asset_object = Asset.objects.get(id=id,).delete()
        return JsonResponse({'message':'asset deleted'})
       
