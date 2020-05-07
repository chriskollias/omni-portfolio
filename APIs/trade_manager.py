from .yfinance_api_interface import YFinanceAPiInterface

def place_trade(symbol, quantity, asset_class, position_type, order_type):
    # create position object associated with current users's portfolio
    pass

def get_trade_info(symbol, quantity, asset_class, position_type, order_type):
    #print('Getting trade info', symbol, quantity, asset_class, position_type, order_type)
    if asset_class == 'STOCK':
        trade_info = get_stock_trade_info(symbol, quantity, position_type, order_type)
        # this should probably return a dict with various parameters
        return trade_info
    elif asset_class is 'FIXED INCOME':
        pass
    elif asset_class is 'FIXED INCOME':
        pass
    elif asset_class is 'CRYPTO':
        pass
    elif asset_class is 'COMMODITY':
        pass
    elif asset_class is 'FOREX':
        pass

def get_stock_trade_info(symbol, quantity, position_type, order_type):
    yfinance_api = YFinanceAPiInterface()
    last_price = yfinance_api.get_previous_close(symbol)
    # this should probably return a dict with various parameters
    return last_price


def place_stock_trade(symbol, quantity, position_type, order_type):
    pass

def place_fixedincome_trade():
    pass

def place_commodity_trade():
    pass

def place_crypto_trade():
    pass

def place_forex_trade():
    pass

