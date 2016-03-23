from .securities_models import Bond
import re

def file_opener():

	bonds = []
	with open('securities/bonds_folder/gov_fixed.csv','r', encoding='utf8',errors='replace') as bonds_data:
		for line in bonds_data.readlines():
			split_line = line.strip().split(',')
			name, symbol, coupon, maturity, *_,sp, moody = split_line
			if not name.startswith('#N/A'):
				bonds.append([name, symbol, coupon, maturity])
		return bonds[1:]


def inser_data_in_db():
		data = file_opener()
		for name, symbol, coupon, maturity in data:
			
			temp_maturity = maturity.split("/")
			year = temp_maturity.pop()
			temp_maturity.insert(0, year)
			maturity = "-".join(temp_maturity)
			if re.search("[a-zA-Z]",maturity):
				pass
			else:
				bond = Bond(
					company_name=name,
					symbol=symbol,
					coupon=coupon,
					maturity_date=maturity,
				)
				bond.save()