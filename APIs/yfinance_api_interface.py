from . import yfinance as yf

class YFinanceAPiInterface():
    def __init__(self):
        pass

    def get_all_market_data(self, ticker):
        market_data = yf.Ticker(ticker)
        return market_data

    def get_previous_close(self, ticker):
        market_data = yf.Ticker(ticker)
        return market_data.info['previousClose']

'''
msft = yf.Ticker("MSFT")

# get stock info
print(msft.info.keys())

# get historical market data
hist = msft.history(period="max")

# show actions (dividends, splits)
msft.actions

# show dividends
msft.dividends

# show splits
msft.splits

# show financials
msft.financials
msft.quarterly_financials

# show major holders
stock.major_holders

# show institutional holders
stock.institutional_holders

# show balance heet
msft.balance_sheet
msft.quarterly_balance_sheet

# show cashflow
msft.cashflow
msft.quarterly_cashflow

# show earnings
msft.earnings
msft.quarterly_earnings

# show sustainability
msft.sustainability

# show analysts recommendations
msft.recommendations

# show next event (earnings, etc)
msft.calendar

# show ISIN code - *experimental*
# ISIN = International Securities Identification Number
msft.isin

# show options expirations
msft.options

# get option chain for specific expiration
opt = msft.option_chain('YYYY-MM-DD')
# data available via: opt.calls, opt.puts
'''

if __name__ == '__main__':
    msft = yf.Ticker("MSFT")

    # get stock info
    print(msft.info.keys())