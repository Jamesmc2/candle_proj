from django.shortcuts import render, redirect
from .models import Candle, Scent
from operator import itemgetter

def shop(request):
    scents = Scent.objects.all()
    context = {
        "scents" : scents
    }
    return render(request, 'shop.html', context)

def cart(request):
    checkout_items = []
    for item in request.session["cart"]:
        candle = Candle.objects.get(id=item["candle_id"])
        new_checkout_item = {
            "candle_name" : candle.name,
            "candle" : candle,
            "quantity" : item["quantity"],
        }
        checkout_items.append(new_checkout_item)

    checkout_sort = sorted(checkout_items, key = itemgetter("candle_name"))
    context = {
        "checkout_items" : checkout_sort,
        "subtotal" : request.session["cart_total"]
    }

    return render(request, 'cart.html', context)

def cart_add(request):
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
    
    cart_quantity = 0
    cart_total = 0
    for item in request.session["cart"]:
        candle = Candle.objects.get(id=item["candle_id"])
        cart_quantity += int(item["quantity"])
        cart_total += int(item["quantity"])*int(candle.price)

    request.session["cart_quantity"] = cart_quantity
    request.session["cart_total"] = cart_total
    request.session.modified = True
    request.session.set_expiry(0)

    return render(request, 'cart_quantity.html')

def cart_update(request):
    if request.method == "POST":
        update_item = next(item for item in request.session["cart"] if item["candle_id"] == request.POST["candle_id"])
        if request.POST["quantity"] == "0":
            request.session["cart"].remove(update_item)
        else:
            update_item["quantity"] = request.POST["quantity"]

    cart_quantity = 0
    cart_total = 0
    for item in request.session["cart"]:
        candle = Candle.objects.get(id=item["candle_id"])
        cart_quantity += int(item["quantity"])
        cart_total += int(item["quantity"])*int(candle.price)

    request.session["cart_quantity"] = cart_quantity
    request.session["cart_total"] = cart_total
    request.session.modified = True
    request.session.set_expiry(0)
    
    # subtotal = 0
    # for item in request.session["cart"]:
    #     candle = Candle.objects.get(id=item["candle_id"])
    #     subtotal += int(item["quantity"])*int(candle.price)

    # context = {
    #     "subtotal" : subtotal
    # }

    # return render(request, 'subtotal.html', context)
    return redirect('/shop/cart')

def checkout(request):

    pass