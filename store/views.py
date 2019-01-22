from django.shortcuts import render
from card.models import Deck, Card, Collection
from store.models import Card_Store, score
from store.forms import StoreForm
from django.contrib.auth.models import User


# Create your views here.

def home(request):
	return render(request, "store/home.html")

def listCardSell(request):
	if request.user :
		current_user = request.user

	if request.method == "POST":
		card = Card.objects.get(id=request.POST.get("card"))
		c = Card_Store(user=current_user, card=card, available="0", point=request.POST.get("price"))

		coll = Collection.objects.get(user_id=request.user.id)
		coll.cards.add(card)

		c.save()
		return render(request, "store/home.html")
	else:
			form = StoreForm()

	cardDecks = Card_Store.objects.filter(available=1).exclude(user=current_user)

	return render(request,
	"store/listCard.html",
	{
		"cardDecks": cardDecks
	})

def sell(request):
	if request.user :
		current_user = request.user

	decks = Deck.objects.filter(id_user=current_user.id)

	if request.GET and request.GET["deck"]:
		idDeck = request.GET['deck']
		cards = Card.objects.filter(collection__user_id=request.user.id)
	else:
		cards = Card.objects.filter(collection__user_id=request.user.id)

		if request.method == "POST":
			card = Card.objects.get(id=request.POST.get("card"))
			c = Card_Store(user=current_user, card=card, available="1", point=request.POST.get("price"))

			coll = Collection.objects.get(user_id=request.user.id)
			coll.cards.remove(card)

			c.save()
			return render(request, "store/home.html")
		else:
			form = StoreForm()

	return render(request,
	"store/sell.html",
	{
	    "decks" : decks,
		"cards": cards,
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
