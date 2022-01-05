from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.conf import settings

from .forms import OrderForm
from bag.contexts import bag_contents

import stripe


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "You currently have no orders")
        return redirect(reverse('packages'))

    current_bag = bag_contents(request)
    total = current_bag['grand_total']
    stripe_total = round(total * 100)

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51K2M88Dz0BPJIeyz0Lx66Re2NVU5sE2syeNbHZEcXURZJtYsn4GdL6u7dYAihdAT93Eg9Ifa84lzm50O4kFFG8xx00ENA8MAIH',
        'client_secret': 'test client secret,'
    }

    return render(request, template, context)
