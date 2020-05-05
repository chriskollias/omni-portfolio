from django.shortcuts import render
from .models import Portfolio, Position
from users.models import UserProfile

def portfolio_dashboard_view(request, *args, **kwargs):
    user_profile = UserProfile.objects.get(user=request.user)
    portfolio = Portfolio.objects.get(user_profile=user_profile)
    portfolio_positions = Position.objects.filter(portfolio=portfolio)

    return render(request, 'portfolio/portfolio_dashboard.html', {'portfolio_positions': portfolio_positions})
