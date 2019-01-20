from django.shortcuts import render
from card.forms import CardForm
from card.models import Card, Deck, Collection
import json
import os
from pprint import pprint
from django.http import HttpResponse

# Create your views here.
def create_deck(request):

	if request.is_ajax():
		if request.method == 'POST':
			card_ids = request.POST.getlist("deck[]")

	if request.method == 'POST': 
		current_user = request.user
		deck_name = "Nom du Deck"
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

def view_collection(request):
	current_user = request.user
	CurrentCollection = Collection.objects.filter(user_id=current_user.id)
	if not CurrentCollection :
		FreeCards = Card.objects.filter(rare="Free").values_list('id', flat=True)
		CardIds = []
		for id in FreeCards :
			CardIds.append(id);
		collection_instance = Collection.objects.create(user_id=current_user.id)
		collection_instance.cards.set(CardIds)
		CurrentCollection = Collection.objects.filter(user_id=current_user.id)

	return render(request,
	"card/view_collection.html",
	{
	    "collections" : CurrentCollection
	})

def import_cards(request):
	module_dir = os.path.dirname(__file__)
	file_path = os.path.join(module_dir, 'cards.json')
	file = open(file_path)

	with file as f:
		data = json.load(f)

	for card in data['Basic']:
		if 'img' in card:
			if card['type'] != 'Hero' :
				card_instance = Card.objects.create(
									name=card['name'], 
									description=card['flavor'] if 'flavor' in card else None,
									cost=card['cost'] if 'cost' in card else None,
									attack_point=card['attack'] if 'attack' in card else None,
									life_point=card['health'] if 'health' in card else None,
									image=card['img'],
									imageGold=card['imgGold'],
									classe=card['playerClass'],
									rare=card['rarity'] if 'rarity' in card else None,
									race=card['race'] if 'race' in card else None,
									cardSet=card['cardSet'],
									artist=card['artist'] if 'artist' in card else None,
								)

	return HttpResponse("Cartes importées");



	

