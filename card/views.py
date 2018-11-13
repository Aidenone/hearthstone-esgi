from django.shortcuts import render
from card.models import Card, Deck
from pprint import pprint

# Create your views here.
def create_deck(request):

	if request.method == 'POST': 
		current_user = request.user
		cards_id = request.POST.getlist('cards')
		deck_name = request.POST.get("deck_name", "")
		deck_instance = Deck.objects.create(name=deck_name, id_user=current_user.id)
		deck_instance.cards.set(cards_id)

		return render(request,
		"card/create_deck.html",
		{
		"test" : cards_id
		})

	cards = Card.objects.all()
	return render(request,
	"card/create_deck.html",
	{
	"cards" : cards
	})

def show_deck(request):

	if request.user :
		current_user = request.user

	decks = Deck.objects.filter(id_user=current_user.id)
	
	return render(request,
	"card/show_deck.html",
	{
	"decks" : decks
	})