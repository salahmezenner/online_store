from django.shortcuts import render, redirect, get_object_or_404
from catalog.models import Product
from .cart import Cart
from django.http import JsonResponse


def cart_detail(request):
    cart = Cart(request)
    return render(request, 'detail.html', {'cart': cart})

from django.views.decorators.http import require_POST

@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    quantity = int(request.POST.get('quantity', 1))
    update_quantity = request.POST.get('update', 'False') == 'True'

    if quantity > product.stock:
        quantity = product.stock  

    cart.add(product=product, quantity=quantity, update_quantity=update_quantity)
    return redirect('cart:cart_detail')

@require_POST
def cart_update_ajax(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    try:
        quantity = int(request.POST.get("quantity", 1))
    except (ValueError, TypeError):
        quantity = 1

    if quantity < 1:
        cart.remove(product)
    else:
        if quantity > product.stock:
            quantity = product.stock
        cart.add(product=product, quantity=quantity, update_quantity=True)

    total = cart.get_total_price()
    return JsonResponse({
        "quantity": quantity,
        "item_total": str(product.price * quantity),
        "cart_total": str(total),
    })


def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')
