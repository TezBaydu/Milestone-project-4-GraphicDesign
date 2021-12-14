from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse
from django.contrib import messages

from packages.models import Package, CompanyDetails


def view_bag(request):
    """ A view to render bag contents page"""

    # package = get_object_or_404(Package, pk=item_id)
    # company_name = request.POST.get('company_name')
    # company_slogan = request.POST.get('company_slogan')
    # company_description = request.POST.get('company_description')
    # company_colors = request.POST.get('company_colors')
    # company_look = request.POST.get('company_look')
    # bag = request.session.get('bag', {})

    # if bag.keys():
    #     bag[item_id] = {}
    #     messages.success(
    #         request, f'Your {package.friendly_name} Logo Package in your bag')
    #     return redirect("view_bag")
    # else:
    #     messages.error(
    #         request, "You have nothing in your bag. ")
    #     return redirect('view_bag')

    # bag[item_id]['company_name'] = company_name
    # bag[item_id]['company_slogan'] = company_slogan
    # bag[item_id]['company_description'] = company_description
    # bag[item_id]['company_colors'] = company_colors
    # bag[item_id]['company_look'] = company_look

    # bag[item_id]['logo_request_number'] = details.logo_request_number

    # request.session['bag'] = bag

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """ Add package and company detail requests to specified package to bag """

    package = get_object_or_404(Package, pk=item_id)
    company_name = request.POST.get('company_name')
    company_slogan = request.POST.get('company_slogan')
    company_description = request.POST.get('company_description')
    company_colors = request.POST.get('company_colors')
    company_look = request.POST.get('company_look')
    bag = request.session.get('bag', {})

    if not bag.keys():
        bag[item_id] = {}
        details = CompanyDetails(
            company_name=company_name, company_slogan=company_slogan,
            company_description=company_description, company_colors=company_colors,
            company_look=company_look)
        details.save()
        messages.success(
            request, f'Added {package.friendly_name} Logo Package to your bag')
    else:
        messages.error(
            request, "You already have an item in the bag and can only order one \
                 at a time. Please edit your bag or if details are good,\
                      proceed to purchase. ")
        return redirect('view_bag')

    bag[item_id]['company_name'] = company_name
    bag[item_id]['company_slogan'] = company_slogan
    bag[item_id]['company_description'] = company_description
    bag[item_id]['company_colors'] = company_colors
    bag[item_id]['company_look'] = company_look

    bag[item_id]['logo_request_number'] = details.logo_request_number

    request.session['bag'] = bag

    return redirect("view_bag")


def adjust_bag(request, item_id):
    """ Edit company detail requests and re-apply package to bag """

    logo_request_number = request.POST.get('logo_request_number')
    company_name = request.POST.get('company_name')
    company_slogan = request.POST.get('company_slogan')
    company_description = request.POST.get('company_description')
    company_colors = request.POST.get('company_colors')
    company_look = request.POST.get('company_look')
    bag = request.session.get('bag', {})

    bag[item_id]['company_name'] = company_name
    bag[item_id]['company_slogan'] = company_slogan
    bag[item_id]['company_description'] = company_description
    bag[item_id]['company_colors'] = company_colors
    bag[item_id]['company_look'] = company_look

    logo_request_number = bag[item_id]['logo_request_number']

    details = get_object_or_404(
        CompanyDetails, logo_request_number=logo_request_number)

    bag[item_id]['logo_request_number'] = details.logo_request_number

    if company_name == details.company_name and company_slogan == \
            details.company_slogan and company_description == \
            details.company_description and company_colors == \
            details.company_colors and company_look == \
            details.company_look:
        messages.error(request, 'No changes have been made.')

    else:
        details = CompanyDetails(
            company_name=company_name, company_slogan=company_slogan,
            company_description=company_description, company_colors=company_colors,
            company_look=company_look)
        details.save()
        messages.success(request, 'Edited Logo request details to your bag')

    return redirect(reverse("view_bag"))


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
