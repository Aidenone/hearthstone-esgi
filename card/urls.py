from django.urls import path

from . import views


urlpatterns = [
    path('create/deck/', views.create_deck),
]