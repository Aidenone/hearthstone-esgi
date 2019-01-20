from django import forms
from .models import Card

class CardForm(forms.ModelForm):
    class Meta:
        model = Card
        fields = ('name', 'description', 'image', 'cost', 'attack_point', 'life_point', 'type_card', 'classe', 'rare', 'race')
