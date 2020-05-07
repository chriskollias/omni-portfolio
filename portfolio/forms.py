from django import forms

class NewTradeForm(forms.Form):
    symbol = forms.CharField()
    quantity = forms.DecimalField(max_digits=10, decimal_places=3)

    ASSET_CLASSES = (
        ('STOCK', 'Stock'),
        ('FIXED_INCOME', 'Fixed Income'),
        ('CRYPTO', 'Cryptocurrency'),
        ('COMMODITY', 'Commodity'),
        ('FOREX', 'Currency'),
    )

    asset_class = forms.ChoiceField(choices=ASSET_CLASSES)


    POSITION_TYPES = (
        ('Long', 'Long'),
        ('Short', 'Short'),
    )

    position_type = forms.ChoiceField(choices=POSITION_TYPES)


    ORDER_TYPES = (
        ('Market', 'Market'),
        ('Limit', 'Limit'),
        ('Stop', 'Stop'),
        ('Stop Limit', 'Stop Limit')
    )

    order_type = forms.ChoiceField(choices=ORDER_TYPES)