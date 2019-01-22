from django import forms
from .models import Card_Store
from card.models import Collection

class StoreForm(forms.ModelForm):
    class Meta:
        model = Card_Store
        fields = ('user', 'date', 'card', 'available', 'point')
        widgets = {'date': forms.HiddenInput, 'user': forms.HiddenInput(), 'available': forms.HiddenInput() }
