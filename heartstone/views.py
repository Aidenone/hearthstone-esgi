from django.shortcuts import render
from store.models import Card_Store, score

def home(request):
    if request.user :
        current_user = request.user
        cardDecks = Card_Store.objects.filter(available=1).exclude(user=current_user)
        point = 0
        return render(request, "home.html", {
            "cardDecks": cardDecks,
            "point": point
        })

    point = 0
    return render(request, "home.html", {
        "point": point
    })

