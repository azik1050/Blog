from django.shortcuts import render, redirect
from .models import AboutPage, AboutPageCarts, AboutPageStaff
from .forms import ContactForm
from django.contrib import messages


def index_about(req):
    main = AboutPage.objects.first()
    carts = AboutPageCarts.objects.filter(page=main)
    staff = AboutPageStaff.objects.filter(page=main)
    context = {
        'main': main,
        'carts': carts,
        'staff': staff
    }
    return render(req, 'contact_about/index_about.html', context)


def index_contact(req):
    if req.method == 'POST':
        form = ContactForm(req.POST)
        if form.is_valid():
            messages.success(req, 'Thank you for your feedback!')
            form.save()
            return redirect('contact')
        else:
            for field, error in form.errors.items():
                messages.warning(req, error)
    else:
        form = ContactForm()
    return render(req, 'contact_about/index_contact.html', {'form': form})