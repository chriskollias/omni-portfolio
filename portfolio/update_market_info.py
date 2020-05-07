from APIs.yfinance_api_interface import YFinanceAPiInterface

'''
do I need this file here?
'''

yfinance_api = YFinanceAPiInterface()
data = yfinance_api.get_previous_close('MSFT')
#print(data)

print(yfinance_api.get_all_market_data('MSFT').info)