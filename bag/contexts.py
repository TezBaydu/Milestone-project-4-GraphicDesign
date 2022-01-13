from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404

from packages.models import Package


def bag_contents(request):

    bag_items = []
    total = 0
    package_count = 0
    bag = request.session.get('bag', {})

    for item_id, item_data in bag.items():
        if (item_data):
            package = get_object_or_404(Package, pk=item_id)
            total += item_data * package.price
            package_count += item_data
            bag_items.append({
                'item_id': item_id,
                'quantity': item_data,
                'package': package,
            })

    grand_total = total

    context = {
        'bag_items': bag_items,
        'total': total,
        'package_count': package_count,
        'grand_total': grand_total,
    }

    return context
