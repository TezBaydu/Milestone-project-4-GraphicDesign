from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .models import UserEnquiry
from .forms import UserEnquiryForm


def enquiries(request):
    """ Enquiry message sent from site """

    if request.method == 'POST':
        form = UserEnquiryForm(request.POST, request.FILES)
        if form.is_valid():
            enquiry = form.save()
            messages.success(request, 'Message sent, We will be in contact with you soon !')
            return redirect(reverse('enquiry', ))
        else:
            messages.error(request, 'Failed to sen message. \
                Please ensure the form is valid.')
    else:
        form = UserEnquiryForm()

    template = 'enquiries/enquiries.html'
    context = {
        'form': form,
    }

    return render(request, template, context)
