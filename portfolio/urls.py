from django.urls import path
from .views import *

urlpatterns = [
    path('', portfolio_dashboard_view, name='portfolio-dashboard'),
    path('dashboard/', portfolio_dashboard_view, name='portfolio-dashboard'),
    path('new-trade/', new_trade_view, name='new-trade'),
    path('new-trade-confirmation/', new_trade_confirmation_view , name='new-trade-confirmation'),
]