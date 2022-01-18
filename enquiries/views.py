from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from .models import UserEnquiry
from .forms import UserEnquiryForm
from profiles.models import UserProfile


def enquiries(request):
    """ Enquiry message sent from site """

    if request.method == 'POST':
        enquiry_form = UserEnquiryForm(request.POST, request.FILES)
        if enquiry_form.is_valid():
            enquiry_form = enquiry_form.save()
            messages.success(
                request, 'Message sent, We will be in contact with you soon !')
            return redirect(reverse('enquiries', ))
            if request.user.is_authenticated:
                try:
                    profile = UserProfile.objects.get(user=request.user)
                    enquiry_form = UserEnquiryForm(initial={
                        'full_name': profile.user.get_full_name(),
                        'email': profile.user.email,
                    })
                except UserProfile.DoesNotExist:
                    enquiry_form = UserEnquiryForm()
            else:
                enquiry_form = UserEnquiryForm()
                messages.error(request, 'Failed to send message. \
                    Please ensure the form is valid.')
    else:
        enquiry_form = UserEnquiryForm()

    print(enquiry_form)

    template = 'enquiries/enquiries.html'
    context = {
        'enquiry_form': enquiry_form,
    }

    return render(request, template, context)
