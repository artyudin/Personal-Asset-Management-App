from .securities_models import Bond
import re


def file_opener():

	files = ['securities/bonds_folder/corp_a_1.csv', 'securities/bonds_folder/corp_a_2.csv', 'securities/bonds_folder/corp_a_3.csv',
				'securities/bonds_folder/corp_a_4.csv', 'securities/bonds_folder/corp_a_5.csv', 'securities/bonds_folder/corp_a_6.csv',
				'securities/bonds_folder/corp_a_7.csv', 'securities/bonds_folder/corp_a_8.csv', 'securities/bonds_folder/corp_a_9.csv',
				'securities/bonds_folder/corp_aa_1.csv', 'securities/bonds_folder/corp_aa_2.csv', 'securities/bonds_folder/corp_aa_3.csv',
				'securities/bonds_folder/corp_aa_4.csv', 'securities/bonds_folder/corp_aa_5.csv', 'securities/bonds_folder/corp_aa_6.csv',
				'securities/bonds_folder/corp_bbb_1.csv', 'securities/bonds_folder/corp_bbb_2.csv', 'securities/bonds_folder/corp_bbb_3.csv',
				'securities/bonds_folder/corp_bbb_4.csv', 'securities/bonds_folder/corp_bbb_5.csv', 'securities/bonds_folder/corp_bbb_6.csv',
				'securities/bonds_folder/corp_bbb_7.csv', 'securities/bonds_folder/corp_bbb_8.csv', 'securities/bonds_folder/corp_bbb_9.csv',
				'securities/bonds_folder/corp_aaa.csv',
		]
	bonds = []

	for csv_file in files:
		with open(csv_file,'r', encoding='utf8',errors='replace') as bonds_data:
			for line in bonds_data.readlines():
				split_line = line.strip().split(',')
				name, symbol, coupon, maturity, *_,sp, moody = split_line
				if not name.startswith('Name'):
					bonds.append([name, symbol, coupon, maturity, sp, moody])
	return bonds


def inser_data_in_db():
		data = file_opener()
		for name, symbol, coupon, maturity, sp, moody in data:
			
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
					sp_rating=sp,
					moody_rating=moody,
				)
				bond.save()