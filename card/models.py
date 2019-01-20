from django.db import models

class Card(models.Model):
    name = models.CharField(max_length=100, blank=True)
    description = models.TextField(max_length=500, blank=True, null=True)
    cost = models.IntegerField(blank=True, null=True)
    attack_point = models.IntegerField(blank=True, null=True)
    life_point = models.IntegerField(blank=True, null=True)
    type_card = models.CharField(max_length=100, blank=True)
    image = models.CharField(max_length=500, blank=True)
    imageGold = models.CharField(max_length=500, blank=True)
    classe = models.CharField(max_length=10, blank=True)
    rare = models.CharField(max_length=10, blank=True, null=True)
    race = models.CharField(max_length=10, blank=True, null=True)
    cardSet = models.CharField(max_length=500, blank=True)
    artist = models.CharField(max_length=500, blank=True, null=True)

    def __str__(self):
        return self.name


class Deck(models.Model):
    name = models.TextField(max_length=50, blank=True)
    id_user = models.IntegerField()
    cards = models.ManyToManyField("Card")



