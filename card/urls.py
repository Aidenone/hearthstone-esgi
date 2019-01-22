from django.urls import path

from . import views

urlpatterns = [
    path('create/deck/', views.create_deck),
    path('create/card/', views.create_card),
    path('show/decks/', views.show_deck),
    path('import-cards/', views.import_cards),
    path('collection/', views.view_collection),
    path('delete/deck/<int:id_deck>', views.delete_deck),

]
