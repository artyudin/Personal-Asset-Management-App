import re
from decimal import Decimal
from pandas_datareader.base import RemoteDataError
from .securities_models import Stock
from analysis.utilities import risk_calc

def file_opener():
    stocks = []
    risk = risk_calc.RiskAnalysis()
    with open('securities/companylist.csv','r',errors='replace') as stock_data:
        count = 0
        for line in stock_data.readlines()[1:]:
            count += 1
            symbol, name, _, marketcap, _, sector, industry, _ = line.split("\n")[0].split('","')
            symbol = symbol[1:].strip()
            try:
                risk.run_analysis(symbol)
            except RemoteDataError as rde:
                print("*"*80,[symbol, name, marketcap, sector, industry],"*"*80,sep='\n')
                continue
            marketcap = parse_marketcap(marketcap)
            stocks.append([symbol, name, marketcap, sector, industry])
        return {'count':count,'stocks':stocks}

def inser_data_in_db():
        data = file_opener()
        # print(data[1])
        Stock.objects.bulk_create([Stock(
                symbol=symbol,
                company_name=name,
                market_capitalization=marketcap,
                sector=sector,
                industry=industry
            ) for symbol, name, marketcap, sector, industry in data.get('stocks')])
        print(data.get('count'))

def parse_marketcap(mp):
    mp_M = re.match(r'^\$.*M$',mp)
    mp_B = re.match(r'^\$.*B$',mp)
    if mp_M is not None:
        return Decimal(mp_M.group()[1:-1])
    elif mp_B is not None:
        return  Decimal(mp_B.group()[1:-1])*1000
    else:
        return Decimal('0.00')



