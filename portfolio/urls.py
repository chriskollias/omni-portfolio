from django.urls import path
from .views import *

urlpatterns = [
    path('dashboard/', portfolio_dashboard_view, name='portfolio-dashboard'),
    path('new-trade/', new_trade_view, name='new-trade'),
]