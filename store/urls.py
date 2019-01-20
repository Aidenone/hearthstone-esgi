from django.urls import path

from . import views

urlpatterns = [
    path('home', views.home, name='store'),
    path('sale', views.sell, name='sale'),
    path('purchase', views.purchase, name='purchase'),
]
