from django.shortcuts import render, get_object_or_404
from .models import Artwork


# Create your views here.
def all_artworks(request):
    """ View to show all artworks """

    artworks = Artwork.objects.all()

    context = {
        'artworks': artworks
    }

    return render(request, 'artworks/artworks.html', context)


def artwork_detail(request, artwork_id):
    """ View to show one artwork """

    artwork = get_object_or_404(Artwork, pk=artwork_id)

    context = {
        'artwork': artwork
    }

    return render(request, 'artworks/artwork_detail.html', context)
