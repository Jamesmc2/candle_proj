from django.db import models
from login_app.models import User



class Candle(models.Model):
    name = models.CharField(max_length = 50)
    desc = models.TextField()
    cat1 = models.CharField(max_length = 25, blank=True)
    cat2 = models.CharField(max_length = 25, blank=True)
    image = models.CharField(max_length = 50)
    in_stock = models.SmallIntegerField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    favorited_by = models.ManyToManyField(User, related_name = "favorites")
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
