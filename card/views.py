from django.shortcuts import render

# Create your views here.
def list_cards(request):
	articles = "test"
	return render(request,
	"card/list_cards.html",
	{
	"articles" : articles
	})