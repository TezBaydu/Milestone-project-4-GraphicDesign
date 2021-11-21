from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from packages.models import Package


def bag_contents(request):

    bag_items = []
    grand_total = 0
    bag = request.session.get('bag', {})
    print(bag)

    for item_id, details in bag.items():
        package = get_object_or_404(Package, pk=item_id)
        bag_items.append({
            'item_id': item_id,
            'package': package,
            'package.price': package.price,
            'company_name': details[0],
            "company_slogan": details[1],
            "company_description": details[2],
            "company_colors": details[3],
            "company_look": details[4],
        })

        grand_total += package.price

    context = {
        'bag_items': bag_items,
        'grand_total': grand_total,
    }

    return context
