from portfolio.models import Portfolio


class ModelPortfolio:

	def __init__(self, score):
		self.score = score

	def recommended_portfolio(self):

		if self.score in [16, 17, 18, 19, 20]:
			return_portfolio = 1
			# return "agre1ssive"

		elif self.score in [11, 12, 13, 14, 15]:
			return_portfolio = 2
			# return "moderatly_aggressive"

		elif self.score in [6, 7, 8, 9, 10]:
			return_portfolio = 3
			# return "moderate"

		else:
			return_portfolio = 4
			# return "conservative"
		return return_portfolio

	
# 	def call_text(self, portfolio_id):

# 		if portfolio_id = '1':
# 			with open('agressive.txt', 'r') as myfile:
# 				data=myfile.read().replace('\n', '')
# 		elif portfolio_id = '2':
# 			with open('moderatly_aggressive.txt', 'r') as myfile:
# 				data=myfile.read().replace('\n', '')
# 		elif portfolio_id = '2':
# 			with open('moderate.txt', 'r') as myfile:
# 				data=myfile.read().replace('\n', '')
# 		else:
# 			with open('moderate.txt', 'r') as myfile:
# 				data=myfile.read().replace('\n', '')
# 		return data

# 	def get_recommendation(self):
# 		return_portfolio = self.recommended_portfolio()
# 		data = self.call_text(return_portfolio.id)
# 		return dict(portfolio=return_portfolio.to_json(), portfolio_description=data)





# # p = Model_portfolio(2)




