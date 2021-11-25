from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from packages.models import Package


def view_bag(request):
    """ A view to render bag contents page"""

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """ Add company detail requests to specified package to bag """

    # package = get_object_or_404(Package, pk=item_id)
    company_name = request.POST.get('company_name')
    company_slogan = request.POST.get('company_slogan')
    company_description = request.POST.get('company_description')
    company_colors = request.POST.get('company_colors')
    company_look = request.POST.get('company_look')
    bag = request.session.get('bag', {})
    # package = request.session.get('package', {})
    
    if not bag.keys():
        bag[item_id] = {}
        messages.success(request, f'Added {package.friendly_name} to bag')
    else:
        messages.error(request, "You already have an item in the bag and can only order one at a time. Please edit your bag or if details are good, proceed to purchase. ")
        return redirect('view_bag')

    # bag[item_id]['package_name'] = package
    bag[item_id]['company_name'] = company_name
    bag[item_id]['company_slogan'] = company_slogan
    bag[item_id]['company_description'] = company_description
    bag[item_id]['company_colors'] = company_colors
    bag[item_id]['company_look'] = company_look

    request.session['bag'] = bag

    return redirect("view_bag")

