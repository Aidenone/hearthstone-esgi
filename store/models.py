from django.db import models
from django.db.models import ForeignKey
from card.models import Card
from django.contrib.auth.models import User
from datetime import datetime

class Card_Store(models.Model):
    user = ForeignKey(User, on_delete=models.CASCADE)
    card = ForeignKey(Card, on_delete=models.CASCADE)
    date = models.DateField()
    point = models.IntegerField()
    available = models.IntegerField()

class score(models.Model):
    user = ForeignKey(User, on_delete=models.CASCADE)
    point = models.IntegerField()
    type = models.IntegerField()
    date = models.DateTimeField(default=datetime.now, blank=True)
