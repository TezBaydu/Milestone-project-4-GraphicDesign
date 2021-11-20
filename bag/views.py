from django.shortcuts import render, redirect


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

    if item_id in list(bag.keys()):
        bag[item_id] += [
            company_name,
            company_slogan,
            company_description,
            company_colors,
            company_look,
        ]
    else:
        bag[item_id] = [
            company_name,
            company_slogan,
            company_description,
            company_colors,
            company_look,
        ]

    request.session['bag'] = bag
    print(request.session['bag'])

    return redirect(redirect_url)
