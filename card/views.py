from django.shortcuts import render
from card.forms import CardForm
from card.models import Card, Deck
import json

# Create your views here.
def create_deck(request):

	if request.is_ajax():
		if request.method == 'POST':
			card_ids = request.POST.getlist("deck[]")

	if request.method == 'POST': 
		current_user = request.user
		deck_name = "test drag and drop"
		deck_instance = Deck.objects.create(name=deck_name, id_user=current_user.id)
		deck_instance.cards.set(card_ids)

		return render(request,
		"card/create_deck.html",
		{
		"test" : card_ids
		})

	cards = Card.objects.all()
	return render(request,
	"card/create_deck.html",
	{
	"cards" : cards
	})

def create_card(request):
    if request.method == "POST":
        form = CardForm(request.POST)
        if form.is_valid():
            card = form.save(commit=False)
            card.save()
        return render(request, 'card/create_deck.html')
    else:
        form = CardForm()
    return render(request, 'card/create_card.html', {'form': form})

def show_deck(request):

	if request.user :
		current_user = request.user

	decks = Deck.objects.filter(id_user=current_user.id)

	return render(request,
	"card/show_deck.html",
	{
	    "decks" : decks
	})
