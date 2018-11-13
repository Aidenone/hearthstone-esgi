from django.db import models

class Card(models.Model):
    name = models.TextField(max_length=50, blank=True)
    description = models.TextField(max_length=500, blank=True)
    image = models.TextField(max_length=500, blank=True)
    cost = models.IntegerField()
    attack_point = models.IntegerField()
    life_point = models.IntegerField()
    type_card = models.CharField(max_length=10, blank=True)
    classe = models.CharField(max_length=10, blank=True)
    rare = models.CharField(max_length=10, blank=True)
    race = models.CharField(max_length=10, blank=True)

    def __str__(self):
        return self.name


class Deck(models.Model):
    name = models.TextField(max_length=50, blank=True)
    id_user = models.IntegerField()
    cards = models.ManyToManyField("Card")



