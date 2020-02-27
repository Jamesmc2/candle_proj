from django.db import models
from login_app.models import User

class Scent(models.Model):
    BEES = "bees_knees_small.jpg"
    FRENCH = "french75.jpg"
    SOUTH = "south_side_fizz.jpg"
    TONIC = "tonic_and_gin.jpg"
    WARD8 = "ward8.jpg"

    IMAGE_CHOICES = [
        (BEES, "Bee's Knees"),
        (FRENCH, "French 75"),
        (SOUTH, "South Side Fizz"),
        (TONIC, "Tonic and Gin"),
        (WARD8, "Ward 8")
    ]
    
    name = models.CharField(max_length = 50)
    desc = models.TextField()
    cat1 = models.CharField(max_length = 25, blank=True)
    cat2 = models.CharField(max_length = 25, blank=True)
    image = models.CharField(max_length = 50, choices = IMAGE_CHOICES, default = BEES)

    def __str__(self):
        return self.name

class Candle(models.Model):

    STYLE_CHOICES = [
        ("Jar", "Jar"),
        ("Melt", "Melt")
    ]

    BEES = "bees_knees_small.jpg"
    FRENCH = "french75.jpg"
    SOUTH = "south_side_fizz.jpg"
    TONIC = "tonic_and_gin.jpg"
    WARD8 = "ward8.jpg"

    IMAGE_CHOICES = [
        (BEES, "Bee's Knees"),
        (FRENCH, "French 75"),
        (SOUTH, "South Side Fizz"),
        (TONIC, "Tonic and Gin"),
        (WARD8, "Ward 8")
    ]

    name = models.CharField(max_length = 100)
    scent = models.ForeignKey(Scent, related_name = "candles", on_delete = models.CASCADE)
    style = models.CharField(max_length = 25, choices = STYLE_CHOICES, default = "Jar")
    image = models.CharField(max_length = 50, choices = IMAGE_CHOICES, default = BEES)
    in_stock = models.SmallIntegerField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    favorited_by = models.ManyToManyField(User, related_name = "favorites")
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return '%s %s' % (self.scent, self.style)