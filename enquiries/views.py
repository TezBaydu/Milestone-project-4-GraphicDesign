from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .models import UserEnquiry
from .forms import UserEnquiryForm


def enquiries(request):
    """ Enquiry message sent from site """

    if request.method == 'POST':
        enquiry_form = UserEnquiryForm(request.POST, request.FILES)
        if enquiry_form.is_valid():
            enquiry_form = enquiry_form.save()
            messages.success(
                request, 'Message sent, We will be in contact with you soon !')
            return redirect(reverse('enquiries', ))
        else:
            messages.error(request, 'Failed to send message. \
                Please ensure the form is valid.')
    else:
        enquiry_form = UserEnquiryForm()

    template = 'enquiries/enquiries.html'
    context = {
        'enquiry_form': enquiry_form,
    }

    return render(request, template, context)
