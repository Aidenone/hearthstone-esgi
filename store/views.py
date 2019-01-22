from django.shortcuts import render
from card.models import Deck
from store.models import Card_Store, score
from store.forms import StoreForm
from django.contrib.auth.models import User
from django.http import HttpResponse, Http404
from inspect import getmembers
from pprint import pprint
from django.forms import formset_factory

# Create your views here.

def home(request):
	return render(request, "store/home.html")

def listCardSell(request):
	if request.user :
		current_user = request.user

	cardDecks = Card_Store.objects.filter(available=1).exclude(user=current_user)

	return render(request,
	"store/listCard.html",
	{
		"cardDecks": cardDecks
	})

def sell(request):
	if request.user :
		current_user = request.user

	decks = Deck.objects.filter(user=current_user)

	if request.GET and request.GET["deck"]:
		idDeck = request.GET['deck']
		cardDecks = Deck.objects.filter(id=idDeck)
	else:
		cardDecks = Deck.objects.filter(id=0)

		if request.method == "POST":
			form = StoreForm(request.POST)

			if form.is_valid():
				store = form
				store.save()

				return render(request, "store/home.html")
		else:
			form = StoreForm()

	return render(request,
	"store/sell.html",
	{
	    "decks" : decks,
		"cardDecks": cardDecks,
		"form": form

	})

def purchase(request):
	return render(request, "store/purchase.html")

def gift(request):
	if request.user :
		current_user = request.user

	#type 0: achat, 1: vente, 2: cadeau
	promo = score.objects.filter(user=current_user, type=2)

	if not promo :
		b = score(user=current_user, point='100', type="2")
		b.save()

	return render(request, "store/gift.html")
