from django.shortcuts import render

from card.forms import CardForm
from card.models import Card

# Create your views here.
def create_deck(request):
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
