from django.shortcuts import render
from .models import Artwork

# Create your views here.
def all_artworks(request):
    """ View to show all artworks """

    artworks = Artwork.objects.all()

    context = {
        'artworks' : artworks
    }

    return render(request, 'artworks/artworks.html', context)
