from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Portfolio, Position
from users.models import UserProfile
from .forms import NewTradeForm
from APIs import trade_manager

@login_required
def portfolio_dashboard_view(request, *args, **kwargs):
    user_profile = UserProfile.objects.get(user=request.user)
    portfolio = Portfolio.objects.get(user_profile=user_profile)
    portfolio_positions = Position.objects.filter(portfolio=portfolio)

    return render(request, 'portfolio/portfolio_dashboard.html', {'portfolio_positions': portfolio_positions})

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
            price_info = trade_manager.get_trade_info(symbol, quantity, asset_class, position_type, order_type)
            print(f'Trade info is {price_info}')
            #return render(request, 'portfolio/new_trade.html', {'form': form, 'trade_info': trade_info})

    form = NewTradeForm()
    return render(request, 'portfolio/new_trade.html', {'form': form})