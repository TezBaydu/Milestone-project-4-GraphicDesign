from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404

from packages.models import Package, CompanyDetails


def bag_contents(request):

    bag_items = []
    grand_total = 0
    bag = request.session.get('bag', {})

    for item_id, details in bag.items():
        package = get_object_or_404(Package, pk=item_id)
        bag_items.append({
            'item_id': item_id,
            'package': package,
            'package.price': package.price,
            'package.friendly_name': package.friendly_name,
            'company_name': details["company_name"],
            'company_slogan': details["company_slogan"],
            'company_description': details["company_description"],
            'company_colors': details["company_colors"],
            'company_look': details["company_look"],
        })
        grand_total += package.price

    context = {
        'bag_items': bag_items,
        'grand_total': grand_total,
    }

    return context
