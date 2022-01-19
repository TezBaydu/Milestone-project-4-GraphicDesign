from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Package
from .forms import PackageForm


def all_packages(request):
    """ A view to show all packages """
    if request.user.is_superuser:
        packages = Package.objects.all()
    else:
        packages = Package.objects.filter(active=True)

    context = {
        'packages': packages,
    }

    return render(request, 'packages/packages.html', context)


def package_detail(request, package_id):
    """ A view to show individual package details """
    if not request.user.is_authenticated:
        messages.info(
            request, "Sorry, You need to login to make a purchase. \
            If you're not registered, \
            please click on the link below to Sign Up!")
        return redirect(reverse('account_login'))
    else:
        package = get_object_or_404(Package, pk=package_id)

        context = {
            'package': package,
        }

        return render(request, 'packages/package_detail.html', context)


@login_required
def add_package(request):
    """ Add a package to the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only Admin can do this.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = PackageForm(request.POST, request.FILES)
        if form.is_valid():
            package = form.save()
            messages.success(request, 'Successfully added package!')
            return redirect(reverse('package_detail', args=[package.id]))
        else:
            messages.error(request, 'Failed to add package. \
                Please ensure the form is valid.')
    else:
        form = PackageForm()

    template = 'packages/add_package.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_package(request, package_id):
    """ Edit a package """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only Admin can do this.')
        return redirect(reverse('home'))

    package = get_object_or_404(Package, pk=package_id)
    if request.method == 'POST':
        form = PackageForm(request.POST, request.FILES, instance=package)
        if form.is_valid():
            form.save()
            messages.success(request, f'Successfully \
                updated {package.name} Package!')
            return redirect(reverse('package_detail', args=[package.id]))
        else:
            messages.error(request, 'Failed to update package. \
                Please ensure form is valid')
    else:
        form = PackageForm(instance=package)
        messages.info(request, f'Your are editing {package.name}')

    template = 'packages/edit_package.html'
    context = {
        'form': form,
        'package': package,
    }

    return render(request, template, context)


@login_required
def deactivate_package(request, package_id):
    """ Deactivate a Package so is not visible \
        to public or registered users but is still stored in orders. """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only Admin can do this.')
        return redirect(reverse('home'))

    package = get_object_or_404(Package, pk=package_id)
    Package.objects.filter(pk=package.pk).update(active=False)
    messages.success(request, f'Package {package.name} is now Deactivated!')
    return redirect(reverse('packages'))


@login_required
def activate_package(request, package_id):
    """ Activate a Package so is visible to public and registered users """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only Admin can do this.')
        return redirect(reverse('home'))

    package = get_object_or_404(Package, pk=package_id)
    Package.objects.filter(pk=package.pk).update(active=True)
    messages.success(request, f'Package {package.name} is now Activated!')
    return redirect(reverse('packages'))
