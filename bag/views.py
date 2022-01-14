from django.shortcuts import (
    render, redirect, reverse, get_object_or_404, HttpResponse)
from django.contrib import messages

from packages.models import Package


def view_bag(request):
    """ A view to render bag contents page"""

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """ Add package and company detail requests to bag """

    quantity = 1
    # get package details, post company details and get empty bag
    package = get_object_or_404(Package, pk=item_id)
    bag = request.session.get('bag', {})

    print(bag)

    # if bag item is empty then apply company details and save to bag
    if item_id in list(bag.keys()):
    # if not item_id:
        bag[item_id] += quantity
        messages.error(
            request, "You already have an item in the bag and can only order one \
                 at a time. Please edit your bag or if details are good,\
                      proceed to purchase. ")
    else:
        bag[item_id] = quantity
        messages.success(
            request, f'Added {package.friendly_name} Logo Package to your bag')
            
    print(quantity)
    request.session['bag'] = bag
    print(bag)
    return redirect('view_bag')


def remove_from_bag(request, item_id):
    """ Delete package from bag """
    try:
        bag = request.session.get('bag', {})

        bag.pop(item_id)

        messages.success(request, 'Item removed from bag')

        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        return HttpResponse(status=500)
