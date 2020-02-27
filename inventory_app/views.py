from django.shortcuts import render, redirect
from .models import Candle

def shop(request):
    candles = Candle.objects.all()
    context = {
        "candles" : candles
    }
    return render(request, 'shop.html', context)

