from django.shortcuts import render
from cart.cart import Cart

from .models import CheckoutSettings, Order, OrderItem
from .utils import format_order_message, send_whatsapp_message

def order_create(request):
    cart = Cart(request)
    for item in cart:
        if item['quantity'] > item['product'].stock:
            error = f"Not enough stock for {item['product'].title}. Only {item['product'].stock} left."
            return render(request, 'checkout/create.html', {'cart': cart, 'error': error})
        
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        phone_number = request.POST.get('phone_number')
        address = request.POST.get('address')
        city = request.POST.get('city')

        if not first_name or not phone_number or not address:
            error = "Please fill in all required fields."
            return render(request, 'checkout/create.html', {'cart': cart, 'error': error})

        # Create order manually
        order = Order.objects.create(
            first_name=first_name,
            last_name=last_name,
            phone_number=phone_number,
            address=address,
            city=city,
        )

        # Create each order item
        notification_items = []
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

            price = item['price']
            notification_items.append(
                f"- {product.title} x {quantity} @ ${price:.2f}"
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

        default_whatsapp_number = CheckoutSettings.get_default_whatsapp_number()
        if default_whatsapp_number and notification_items:
            message = format_order_message(order, notification_items)
            send_whatsapp_message(default_whatsapp_number, message)

        return render(request, 'checkout/created.html', {'order': order})

    return render(request, 'checkout/create.html', {'cart': cart})
