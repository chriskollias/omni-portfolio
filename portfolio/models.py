from django.db import models
from users.models import UserProfile

class Portfolio(models.Model):
    user_profile = models.OneToOneField(UserProfile, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user_profile.user.username} Portfolio'


class Position(models.Model):
    '''
    An investment position
    '''

    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE)

    ASSET_CLASSES = (
        ('STOCK', 'Stock'),
        ('FIXED_INCOME', 'Fixed Income'),
        ('CRYPTO', 'Cryptocurrency'),
        ('COMMODITY', 'Commodity'),
        ('FOREX', 'Currency'),
    )
    asset_class = models.CharField(max_length=15, choices=ASSET_CLASSES)
    position_symbol = models.CharField(max_length=120)

    POSITION_TYPES = (
        ('L', 'Long'),
        ('S', 'Short'),
    )

    position_type = models.CharField(max_length=1, choices=POSITION_TYPES)
    position_size = models.DecimalField(max_digits=10, decimal_places=3)
    position_created = models.DateTimeField()
    position_status = models.CharField(max_length=120)
    position_entered_price = models.DecimalField(max_digits=11, decimal_places=4, null=True)
    position_exited_price = models.DecimalField(max_digits=11, decimal_places=4, null=True)

    def __str__(self):
        return f'{self.portfolio.user_profile.user.username}: {self.position_type} {self.position_symbol} x {self.position_size}'
