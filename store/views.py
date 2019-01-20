from django.shortcuts import render

# Create your views here.

def home(request):
	return render(request, "store/home.html")

def sell(request):
	return render(request, "store/sell.html")

def purchase(request):
	return render(request, "store/purchase.html")
