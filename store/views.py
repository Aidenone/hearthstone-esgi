from django.shortcuts import render
from card.models import Card, Deck, Collection
from django.http import HttpResponse, Http404

# Create your views here.

def home(request):
	return render(request, "store/home.html")

def sell(request):
	if request.user :
		current_user = request.user

	decks = Deck.objects.filter(id_user=current_user.id)

	if request.GET and request.GET["deck"]:
		idDeck = request.GET['deck']
		cardDecks = Deck.objects.filter(id=idDeck)
	else:
		cardDecks = Deck.objects.filter(id=0)


	return render(request,
	"store/sell.html",
	{
	    "decks" : decks,
		"cardDecks": cardDecks
	})

def purchase(request):
	return render(request, "store/purchase.html")
