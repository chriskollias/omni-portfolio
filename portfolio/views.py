import simplejson as json
from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Portfolio, Position
from users.models import UserProfile
from .forms import NewTradeForm
from APIs import trade_manager

@login_required
def portfolio_dashboard_view(request, *args, **kwargs):
    user_profile = UserProfile.objects.get(user=request.user)
    portfolio = Portfolio.objects.get(user_profile=user_profile)
    cash_available = portfolio.cash_available
    portfolio_positions = Position.objects.filter(portfolio=portfolio)

    return render(request, 'portfolio/portfolio_dashboard.html', {'portfolio_positions': portfolio_positions, 'cash_available': cash_available})

@login_required
def new_trade_view(request, *args, **kwargs):

    if request.method == 'POST':
        form = NewTradeForm(request.POST)
        if form.is_valid():
            symbol = form.cleaned_data['symbol']
            quantity = form.cleaned_data['quantity']
            asset_class = form.cleaned_data['asset_class']
            position_type = form.cleaned_data['position_type']
            order_type = form.cleaned_data['order_type']
            price = trade_manager.get_trade_info(symbol, quantity, asset_class, position_type, order_type)

            # convert price and quantity into JSON so they can be serialized
            price_json = json.dumps(price)
            quantity_json = json.dumps(quantity)
            request.session['price'] = price_json
            request.session['symbol'] = symbol
            request.session['quantity'] = quantity_json
            request.session['asset_class'] = asset_class
            request.session['position_type'] = position_type
            request.session['order_type'] = order_type
            return redirect('new-trade-confirmation')

    form = NewTradeForm()
    return render(request, 'portfolio/new_trade.html', {'form': form})

@login_required
def new_trade_confirmation_view(request, *args, **kwargs):
    trade_errors = None
    trade_info = {}
    try:
        trade_info['price'] = json.loads(request.session['price'], use_decimal=True)
        trade_info['symbol'] = request.session['symbol']
        trade_info['quantity'] = json.loads(request.session['quantity'], use_decimal=True)
        trade_info['asset_class'] = request.session['asset_class']
        trade_info['position_type'] = request.session['position_type']
        trade_info['order_type'] = request.session['order_type']
        trade_info['total'] = trade_info['price'] * trade_info['quantity']
    except:
        trade_errors = "Error: Cannot retrieve trade info. Please return to the trade screen and try again."
    if request.method == 'POST':
        user_profile = UserProfile.objects.get(user=request.user)
        portfolio = Portfolio.objects.get(user_profile=user_profile)
        result = trade_manager.place_trade(trade_info, portfolio)

        print('result:', result)
        if result['new_trade']:
            messages.success(request, "Trade has been placed successfully!")
        else:
            messages.error(request, "There was an error placing your trade:\n" + str(result['trade_errors']))
        return redirect('portfolio-dashboard')
    return render(request, 'portfolio/new_trade_confirmation.html', {'trade_info': trade_info, 'trade_errors': trade_errors})