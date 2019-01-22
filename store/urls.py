from django.urls import path

from . import views

urlpatterns = [
    path('home', views.home, name='store'),
    path('sale', views.sell, name='sale'),
    path('listCard', views.listCardSell, name='listCard'),
    path('gift', views.gift, name='gift'),
    path('purchase', views.purchase, name='purchase')
]
