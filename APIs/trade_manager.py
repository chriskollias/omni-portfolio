from datetime import datetime
from .yfinance_api_interface import YFinanceAPiInterface
from portfolio.models import Position

def place_trade(trade_params, portfolio):
    asset_class = trade_params['asset_class']
    symbol = trade_params['symbol']
    quantity = trade_params['quantity']
    position_type = trade_params['position_type']
    order_type = trade_params['order_type']
    price = trade_params['price']
    try:
        new_trade = Position(portfolio=portfolio, asset_class=asset_class, position_symbol=symbol, position_type=position_type, order_type=order_type, position_size=quantity, position_created=datetime.now(), position_status='filled', position_entered_price=price)
        new_trade.save()
        return new_trade
    except:
        return None

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

