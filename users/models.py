from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    # extends the User model so we can add more fields
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)
    email = models.EmailField(max_length=120)
    city = models.CharField(max_length=120)

    def __str__(self):
        return self.user.username