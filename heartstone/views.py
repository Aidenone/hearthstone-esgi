from django.shortcuts import render
from store.models import Card_Store, score

def home(request):
    point = 0

    if request.user.is_authenticated :
        current_user = request.user
        cardDecks = Card_Store.objects.filter(available=1).exclude(user=current_user)
        return render(request, "home.html", {
            "cardDecks": cardDecks,
            "point": point
        })

    return render(request, "home.html", {
        "point": point
    })

