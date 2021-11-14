from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .models import Package
from .forms import OrderForm

def all_packages(request):
    """ A view to show Case Studies including filtering """

    packages = Package.objects.all()

    if request.GET:
        packages = request.GET['package']

    context = {
        'packages': packages,
    }

    return render(request, 'packages/packages.html', context)


def orders(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There re no orders at the moment")
        return redirect(reverse('orders'))

    order_form = OrderForm()
    template = 'orders/orders.html'
    context = {
        'order_form': order_form,
    }

    return render(request, template, context)
