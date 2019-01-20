from django.db import models
from django.db.models import ForeignKey
from card.models import Card

class Store(models.Model):
    id_user = models.IntegerField()
    price = models.IntegerField()
    old_price = models.IntegerField()
    id_card = ForeignKey(Card, on_delete=models.CASCADE)
    date = models.DateField()
    available = models.IntegerField()
