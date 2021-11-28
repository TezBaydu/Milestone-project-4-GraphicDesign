from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse
from django.contrib import messages

from packages.models import Package, CompanyDetails


def view_bag(request):
    """ A view to render bag contents page"""

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """ Add package and company detail requests to specified package to bag """

    package = get_object_or_404(Package, pk=item_id)
    # company_details = get_object_or_404(CompanyDetails, pk=item_id)
    company_name = request.POST.get('company_name')
    company_slogan = request.POST.get('company_slogan')
    company_description = request.POST.get('company_description')
    company_colors = request.POST.get('company_colors')
    company_look = request.POST.get('company_look')
    bag = request.session.get('bag', {})
    # package = request.session.get('package', {})
    # package = request.POST.get('friendly_name')

    if not bag.keys():
        bag[item_id] = {}
        messages.success(
            request, f'Added {package.friendly_name} Logo Package to your bag')
    else:
        messages.error(
            request, "You already have an item in the bag and can only order one at a time. Please edit your bag or if details are good, proceed to purchase. ")
        return redirect('view_bag')

    # bag[item_id]['package'] = package
    bag[item_id]['company_name'] = company_name
    bag[item_id]['company_slogan'] = company_slogan
    bag[item_id]['company_description'] = company_description
    bag[item_id]['company_colors'] = company_colors
    bag[item_id]['company_look'] = company_look

    # details = CompanyDetails(
    #     company_name=company_name, company_slogan=company_slogan,
    #     company_description=company_description, company_colors=company_colors, company_look=company_look)
    # details.save()

    request.session['bag'] = bag

    return redirect("view_bag")


def adjust_bag(request, item_id):
    """ Edit company detail requests and re-apply package to bag """

    package = get_object_or_404(Package, pk=item_id)
    # company_details = get_object_or_404(CompanyDetails, pk=item_id)
    company_name = request.POST.get('company_name')
    company_slogan = request.POST.get('company_slogan')
    company_description = request.POST.get('company_description')
    company_colors = request.POST.get('company_colors')
    company_look = request.POST.get('company_look')
    bag = request.session.get('bag', {})
    # package = request.session.get('package', {})
    # package = request.POST.get('friendly_name')

    details = CompanyDetails(
        company_name=company_name, company_slogan=company_slogan,
        company_description=company_description, company_colors=company_colors, company_look=company_look)
    details.save()

    # bag[item_id]['package'] = package
    bag[item_id]['company_name'] = company_name
    bag[item_id]['company_slogan'] = company_slogan
    bag[item_id]['company_description'] = company_description
    bag[item_id]['company_colors'] = company_colors
    bag[item_id]['company_look'] = company_look

    request.session['bag'] = bag

    return redirect("view_bag")


def remove_from_bag(request, item_id):
    """ Delete package from bag """
    # try:
    #     package = get_object_or_404(Package, pk=item_id)
    #     company_name = request.POST.get('company_name')
    #     company_slogan = request.POST.get('company_slogan')
    #     company_description = request.POST.get('company_description')
    #     company_colors = request.POST.get('company_colors')
    #     company_look = request.POST.get('company_look')
    #     bag = request.session.get('bag', {})

    #     bag.pop(item_id)

    #     bag.pop[item_id]['company_name'] = company_name
    #     bag.pop[item_id]['company_slogan'] = company_slogan
    #     bag.pop[item_id]['company_description'] = company_description
    #     bag.pop[item_id]['company_colors'] = company_colors
    #     bag.pop[item_id]['company_look'] = company_look
        
    #     messages.success(request, f'Removed {package.friendly_name} Logo Package from your bag')
        
    #     request.session['bag'] = bag
    #     return HttpResponse(status=200)

    # except Exception as e:
    #     return HttpResoinse(status=500)
