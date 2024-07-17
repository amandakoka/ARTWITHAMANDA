from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from artworks.models import Artwork


def bag_contents(request):
    """Context processor to provide information about the bag contents and
    calculate totals"""

    bag_items = []
    total = Decimal('0.00')
    artwork_count = 0
    bag = request.session.get('bag', {})

    for artwork_id, quantity in bag.items():
        artwork = get_object_or_404(Artwork, pk=artwork_id)
        total += quantity * artwork.price
        artwork_count += quantity
        bag_items.append({
            'artwork_id': artwork_id,
            'quantity': quantity,
            'artwork': artwork,
        })

    delivery = Decimal('0.00')
    free_delivery_threshold = settings.FREE_DELIVERY_THRESHOLD

    if total < free_delivery_threshold:
        delivery = settings.STANDARD_DELIVERY_COST
    else:
        delivery = Decimal('0.00')

    grand_total = total + delivery

    context = {
        'bag_items': bag_items,
        'total': total,
        'artwork_count': artwork_count,
        'delivery': delivery,
        'free_delivery_threshold': free_delivery_threshold,
        'grand_total': grand_total,
    }

    return context
