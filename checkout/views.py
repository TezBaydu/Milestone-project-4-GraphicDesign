from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.conf import settings

from .forms import OrderForm
from .models import Order, OrderLineItem
# from packages.models import CompanyDetails
from bag.contexts import bag_contents

# import stripe


def checkout(request):
    # stripe_public_key = settings.STRIPE_PUBLIC_KEY
    # stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == 'POST':
        bag = request.session.get('bag', {})

        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'country': request.POST['country'],
            'postcode': request.POST['postcode'],
            'town_or_city': request.POST['town_or_city'],
            'street_address1': request.POST['street_address1'],
            'street_address2': request.POST['street_address2'],
            'county': request.POST['county'],
        }
        order_form = OrderForm(form_data)
        if order_form.is_valid():
            order = order_form.save()
            for item_id, details in bag.items():
                try:
                    package = Package.objects.get(id=item_id)
                    if isinstance(details, int):
                        order_line_item = OrderLineItem(
                            order=order,
                            package=package,
                            company_name=details.company_name,
                            company_slogan=details.company_slogan,
                            company_description=details.company_description,
                            company_colors=details.company_colors,
                            company_look=details.company_look,
                        )
                        order_line_item.save()
                except Package.DoesNotExist:
                    messages.error(request, (
                        "Package wasn't found in our database."
                        "Please call for assistance!")
                    )
                    order.delete()
                    return redirect(reverse('view_bag'))
            request.session['save_info'] = 'save-info' in request.POST
            return redirect(reverse('checkout_success', args=[order.order_number]))
        else:
            messages.error(request, 'There was an error with your form. \
                Please double check your information.')
                    # package = get_object_or_404(Package, pk=item_id)
                    # bag_items.append({
                    #     'item_id': item_id,
                    #     'package': package,
                    #     'package.price': package.price,
                    #     'package.friendly_name': package.friendly_name,
                    #     'company_name': details["company_name"],
                    #     'company_slogan': details["company_slogan"],
                    #     'company_description': details["company_description"],
                    #     'company_colors': details["company_colors"],
                    #     'company_look': details["company_look"],
                    # })
                    # grand_total += package.price
                    # order_line_item.save()
<<<<<<< HEAD
    else:
        bag = request.session.get('bag', {})
        if not bag:
            messages.error(request, "You currently have no orders")
            return redirect(reverse('packages'))

        # current_bag = bag_contents(request)
        # total = current_bag['grand_total']
        # stripe_total = round(total * 100)
        # stripe.api_key = stripe_secret_key
        # intent = stripe.PaymentIntent.create(
        #     amount=stripe_total,
        #     currency=settings.STRIPE_CURRENCY,
        # )
=======
    # else:
    #     bag = request.session.get('bag', {})
    #     if not bag:
    #         messages.error(request, "You currently have no orders")
    #         return redirect(reverse('packages'))

    #     current_bag = bag_contents(request)
    #     total = current_bag['grand_total']
    #     stripe_total = round(total * 100)
    #     stripe.api_key = stripe_secret_key
    #     intent = stripe.PaymentIntent.create(
    #         amount=stripe_total,
    #         currency=settings.STRIPE_CURRENCY,
    #     )
>>>>>>> 45c01d28b6e9efe2d05870335c15ee2444f6bfac

        # order_form = OrderForm()

    # if not stripe_public_key:
    #     messages.warning(request, 'Stripe public key is missing. \
    #         Did you forget to set it in your environment?')

    # template = 'checkout/checkout.html'
    # context = {
    #     'order_form': order_form,
    #     'stripe_public_key': stripe_public_key,
    #     'client_secret': intent.client_secret,
    # }

    return render(request, template, context)


def checkout_success(request, order_number):
    """ 
    Handle successful checkouts
    """
    save_info = request.session.get('save_info')
    order = get_object_or_404(Order, order_number=order_number)
    messages.success(request, f'Order successfully processed! \
        Your order number is {order_number}. A confirmation \
            email will be sent to {order.email}.')

    if 'bag' in request.session:
        del request.session['bag']

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
    }

    return render(request, template, context)
