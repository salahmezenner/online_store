from django.shortcuts import render, redirect
from cart.cart import Cart
from .models import Order, OrderItem

def order_create(request):
    cart = Cart(request)
    for item in cart:
        if item['quantity'] > item['product'].stock:
            error = f"Not enough stock for {item['product'].title}. Only {item['product'].stock} left."
            return render(request, 'checkout/create.html', {'cart': cart, 'error': error})
        
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        city = request.POST.get('city')

        if not first_name or not email or not address:
            error = "Please fill in all required fields."
            return render(request, 'create.html', {'cart': cart, 'error': error})

        # Create order manually
        order = Order.objects.create(
            first_name=first_name,
            last_name=last_name,
            email=email,
            address=address,
            city=city,
        )

        # Create each order item
        for item in cart:
            product = item['product']
            quantity = item['quantity']

            # Create the order item
            OrderItem.objects.create(
                order=order,
                product=product,
                price=item['price'],
                quantity=quantity
            )

            # 🔻 Reduce stock
            if product.stock >= quantity:
                product.stock -= quantity
                product.save()
            else:
                # Optional: handle out-of-stock scenario gracefully
                print(f"⚠️ Not enough stock for {product.title}!")


        # Clear the cart after placing order
        cart.clear()

        return render(request, 'created.html', {'order': order})

    return render(request, 'create.html', {'cart': cart})
