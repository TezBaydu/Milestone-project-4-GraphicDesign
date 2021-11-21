from django.shortcuts import render, redirect
from django.contrib import messages

from packages.models import Package


def view_bag(request):
    """ A view to render bag contents page"""

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """ Add company detail requests to specified package to bag """

    company_name = request.POST.get('company_name')
    company_slogan = request.POST.get('company_slogan')
    company_description = request.POST.get('company_description')
    company_colors = request.POST.get('company_colors')
    company_look = request.POST.get('company_look')
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})
    
    if not bag.keys():
        bag[item_id] = {}
        messages.success(request, f"Added {item.package.name}to your bag")
    else:
        messages.error(request, "You already have an item in the bag and can only order one at a time. Please edit your bag or if details are good proceed to purchase. ")
        return redirect('view_bag')

    bag[item_id]['company_name'] = company_name
    bag[item_id]['company_slogan'] = company_slogan
    bag[item_id]['company_description'] = company_description
    bag[item_id]['company_colors'] = company_colors
    bag[item_id]['company_look'] = company_look

    request.session['bag'] = bag

    return redirect("view_bag")
