from django.shortcuts import render, redirect
from .models import Candle, Scent

def shop(request):
    scents = Scent.objects.all()
    context = {
        "scents" : scents
    }
    return render(request, 'shop.html', context)

def cart(request):
    if "cart" not in request.session:
        request.session["cart"] = []
        new_cart_item = {
            "candle_id" : request.POST["candle_id"],
            "quantity" : request.POST["quantity"]
        }
        request.session["cart"].append(new_cart_item)
    else:
        update_item = next((item for item in request.session["cart"] if item["candle_id"] == request.POST["candle_id"]), None)
        if update_item == None:
            new_cart_item = {
                "candle_id" : request.POST["candle_id"],
                "quantity" : request.POST["quantity"]
            }
            request.session["cart"].append(new_cart_item)
        else:
            update_item["quantity"] = int(update_item["quantity"]) + int(request.POST["quantity"])
            
    request.session.modified = True
    request.session.set_expiry(0)

    return redirect("/shop")

def checkout(request):
    checkout_items = []
    subtotal = 0
    for item in request.session["cart"]:
        candle = Candle.objects.get(id=item["candle_id"])
        new_checkout_item = {
            "candle" : candle,
            "quantity" : item["quantity"],
            "total" : int(item["quantity"])*int(candle.price)
        }
        checkout_items.append(new_checkout_item)
        subtotal += int(item["quantity"])*int(candle.price)

    context = {
        "checkout_items" : checkout_items,
        "subtotal" : subtotal
    }

    return render(request, 'checkout.html', context)

def update(request):
    update_item = next(item for item in request.session["cart"] if item["candle_id"] == request.POST["candle_id"])
    
    if request.POST["quantity"] == "0":
        request.session["cart"].remove(update_item)
    else:
        update_item["quantity"] = request.POST["quantity"]
    
    request.session.modified = True
    request.session.set_expiry(0)

    return redirect("/shop/checkout")
