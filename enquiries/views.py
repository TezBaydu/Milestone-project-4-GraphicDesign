from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail, mail_admins
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
            send_mail(
                f'Kingsland Design Confirmation for Enquiry \
                    {enquiry_form.enquiry_number}',

                f'Hello {enquiry_form.full_name}! \
                    This is a confirmation of your enquiry with Kingsland Design. \
                        Your message information is below \
                            and we will be in contact with you soon: \
                Message: "{enquiry_form.message}" \
                If you have any questions, \
                    feel free to contact us at {settings.DEFAULT_FROM_EMAIL}, \
                Thank you for your enquiry! \
                Sincerely, \
                Kingsland Design',
                settings.DEFAULT_FROM_EMAIL,
                [f'{enquiry_form.email}'],
                fail_silently=False,
            )
            mail_admins(
                f'Enquiry {enquiry_form.enquiry_number} Received',
                f'Message: {enquiry_form.message}',
                fail_silently=False,
                connection=None,
                html_message=None
            )
            print(send_mail)
            print(mail_admins)
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
