from django.shortcuts import render, redirect, get_object_or_404
from artworks.models import Artwork

# Create your views here.


def view_bag(request):
    """ A view that renders the bag contents page """
    return render(request, 'bag/bag.html')


def add_to_bag(request, artwork_id):
    """ Add a quantity of the specified artwork to the shopping bag """
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if artwork_id in list(bag.keys()):
        bag[artwork_id] += quantity
    else:
        bag[artwork_id] = quantity

    request.session['bag'] = bag
    return redirect(redirect_url)
