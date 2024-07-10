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

    for item_id, quantity in bag.items():
        artworks = get_object_or_404(Artwork, pk=item_id)
        total += quantity * artworks.price
        artwork_count += quantity
        bag_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'artworks': artworks,
        })

    delivery = Decimal('0.00')

    grand_total = total

    context = {
        'bag_items': bag_items,
        'total': total,
        'artwork_count': artwork_count,
        'delivery': delivery,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total,
    }

    return context
