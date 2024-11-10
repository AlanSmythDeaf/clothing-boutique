from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51QJIaPEyQSnrLymRNcjWSjl0BjtsiKlNu4Yc1PxP9dhaHpGUuMD3xVf2uySUML2XK3XCurOubojlJPJ8GjToy2X500T6PR9u51',
        'client_secret': 'text client secret',
    }

    return render(request, template, context)