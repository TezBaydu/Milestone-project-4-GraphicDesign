from django.shortcuts import render
from .models import Package

def all_packages(request):
    """ A view to show Case Studies including filtering """

    packages = Package.objects.all()

    if request.GET:
        packages = request.GET['package']

    context = {
        'packages': packages,
    }

    return render(request, 'packages/packages.html', context)
