from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages

from artworks.models import Artwork


def view_bag(request):
    """ A view that renders the bag contents page """
    return render(request, 'bag/bag.html')


def add_to_bag(request, artwork_id):
    """ Add a quantity of the specified artwork to the shopping bag """

    artwork = get_object_or_404(Artwork, pk=artwork_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if artwork_id in list(bag.keys()):
        bag[artwork_id] += quantity
        messages.success(request, f'Updated {artwork.name} quantity to {bag[artwork_id]}')
    else:
        bag[artwork_id] = quantity
        messages.success(request, f'Added {artwork.name} to your bag')

    request.session['bag'] = bag
    return redirect(redirect_url)


def adjust_bag(request, artwork_id):
    """ Adjust the quantity of the specified artwork in the shopping bag """

    artwork = get_object_or_404(Artwork, pk=artwork_id)
    quantity = int(request.POST.get('quantity'))
    bag = request.session.get('bag', {})

    if quantity > 0:
        bag[artwork_id] = quantity
        messages.success(request, f'Updated {artwork.name} quantity to {bag[artwork_id]}')
    else:
        bag.pop(artwork_id, None)
        messages.success(request, f'Removed {artwork.name} from your bag')

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


def remove_from_bag(request, artwork_id):
    """ Remove the specified artwork from the shopping bag """

    artwork = get_object_or_404(Artwork, pk=artwork_id)
    bag = request.session.get('bag', {})

    if artwork_id in bag:
        bag.pop(artwork_id, None)
        messages.success(request, f'Removed {artwork.name} from your bag')
    else:
        messages.warning(request, f'{artwork.name} was not found in your bag')

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))
