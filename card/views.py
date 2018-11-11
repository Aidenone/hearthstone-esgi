from django.shortcuts import render
from card.models import Card

# Create your views here.
def create_deck(request):
	cards = Card.objects.all()
	return render(request,
	"card/create_deck.html",
	{
	"cards" : cards
	})