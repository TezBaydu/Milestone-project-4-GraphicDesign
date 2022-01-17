from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from .models import Package
from .forms import PackageForm


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

    context = {
        'package': package,
    }

    return render(request, 'packages/package_detail.html', context)


def add_package(request):
    """ Add a package to the store """
    if request.method == 'POST':
        form = PackageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added package!')
            return redirect(reverse('add_package'))
        else:
            messages.error(request, 'Failed to add package. Please ensure the form is valid.')
    else:
        form = PackageForm()

    template = 'packages/add_package.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


def edit_package(request, package_id):
    """ Edit a pacakge """
    package = get_object_or_404(Package, pk=package_id)
    if request.method == 'POST':
        form = PackageForm(request.POST, request.FILES, instance=package)
        if form.is_valid():
            form.save()
            messages.success(request, f'Successfully updated {package.name} Package!')
            return redirect(reverse('packages'))
        else:
            messages.error(request, 'Failed to update package. Please ensure form is valid')
    else:
        form = PackageForm(instance=package)
        messages.info(request, f'Your are editing {package.name}')

    template = 'packages/edit_package.html'
    context = {
        'form': form,
        'package': package,
    }

    return render(request, template, context)
