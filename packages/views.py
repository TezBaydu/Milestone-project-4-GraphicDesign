from django.shortcuts import render, get_object_or_404
from .models import Package, CompanyDetails


def all_packages(request):
    """ A view to show all packages """

    packages = Package.objects.all()

    context = {
        'packages': packages,
    }

    return render(request, 'packages/packages.html', context)


def package_detail(request, package_id):
    """ A view to show individual package details """

    package = get_object_or_404(Package, pk=package_id)
    # company_details = CompanyDetails.objects.all()

    context = {
        'package': package,
        # 'company_details': company_details,
    }

    # print(company_details)

    return render(request, 'packages/package_detail.html', context)


# def company_details(request):
#     """ A view to show company specified logo request details """

#     company_details = CompanyDetails.objects.all()

#     context = {
#         'company_details': company_details,
#     }

#     return render(request, 'packages/packages.html', context)
