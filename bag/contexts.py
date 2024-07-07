from decimal import Decimal
from django.conf import settings


def bag_contents(request):
    """Context processor to provide information about the bag contents and
    calculate totals"""

    bag_items = []
    total = Decimal('0.00')
    artwork_count = 0

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
