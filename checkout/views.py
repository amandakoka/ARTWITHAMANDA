from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm

# Create your views here.


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('artworks'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51PfJtZHul12GLcCBxmzVIvALBAdOc2LUHH7NofrIjlAmdoz3yluWSjB8Y1Cc1RlxTCBV1xmNIQQCglyLmB71C2w900KeSZXJcc',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
