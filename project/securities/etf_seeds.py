from .securities_models import ExchangeTradedFund
from analysis.utilities import risk_calc
from pandas_datareader.base import RemoteDataError



def file_opener():
	etfs = []
	risk = risk_calc.RiskAnalysis()
	with open('securities/etf.csv','r',errors='replace') as etf_data:
		count = 0
		for line in etf_data.readlines():
			count += 1
			split_line = line.strip().split(',')
			name, symbol, type_ = split_line

			if parse_symbol(symbol):
				symbol = symbol.strip()
				try:
					risk.run_analysis(symbol)
				except RemoteDataError as rde:
					print("*"*80,split_line,"*"*80,sep='\n')
					continue
				parent, etf_name = parse_name(name)
				new_etf = [name, parent,  symbol, type_]
				etfs.append(new_etf)
		return {'count': count, 'etfs':etfs}

def parse_name(name):
	parent, *name = name.split(' ')
	return parent, ' '.join(name)


def parse_symbol(symbol):
	if symbol.startswith('$'):
		return False
	elif symbol.startswith('.'):
		return False
	elif symbol.startswith('^'):
		return False
	else:
		return True
			



def insert_data_in_db():
		data = file_opener()
		ExchangeTradedFund.objects.bulk_create([ExchangeTradedFund(
				symbol=symbol,
				name=name,
				category=type_,
				fund_family=family_name,
			) for name, family_name, symbol, type_ in data.get('etfs')])
		
		print(data.get('count'))
		