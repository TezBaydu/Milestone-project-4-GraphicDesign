from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from .models import UserEnquiry
from .forms import UserEnquiryForm
from profiles.models import UserProfile


def enquiries(request):
    """ Enquiry message sent from site """

    if request.method == 'POST':
        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'message': request.POST['message'],
        }
        enquiry_form = UserEnquiryForm(form_data)
        if enquiry_form.is_valid():
            enquiry_form = enquiry_form.save()
            messages.success(
                request, 'Message sent, We will be in contact with you soon !')
            print(enquiry_form)
            return redirect("home")
        else:
            enquiry_form = UserEnquiryForm()
            messages.error(request, 'Failed to send message. \
                Please ensure the form is valid.')
    else:
        if request.user.is_authenticated:
            profile = UserProfile.objects.get(user=request.user)

            enquiry_form = UserEnquiryForm(initial={
                'full_name': profile.default_full_name,
                'email': profile.user.email,
            })
            print(enquiry_form)
        else:
            enquiry_form = UserEnquiryForm()

    template = 'enquiries/enquiries.html'
    context = {
        'enquiry_form': enquiry_form,
    }

    return render(request, template, context)
