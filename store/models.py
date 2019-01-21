from django.db import models
from django.db.models import ForeignKey
from card.models import Card, Deck
from django.contrib.auth.models import User


class exchange(models.Model):
    id_user = ForeignKey(User, on_delete=models.CASCADE)
    point = models.IntegerField()
    id_card = ForeignKey(Card, on_delete=models.CASCADE)
    date = models.DateField()
    available = models.IntegerField()

class Card_Store(models.Model):
    id_deck = ForeignKey(Deck, on_delete=models.CASCADE)
    id_user = ForeignKey(User, on_delete=models.CASCADE)
    id_card = ForeignKey(Card, on_delete=models.CASCADE)
    date = models.DateField()

class score(models.Model):
    id_user = ForeignKey(User, on_delete=models.CASCADE)
    point = models.IntegerField()
    type = models.IntegerField()
    date = models.DateField()
